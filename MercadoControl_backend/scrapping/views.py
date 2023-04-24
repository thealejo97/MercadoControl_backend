from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

from MercadoControl_Backend.list_of_prices.models import List_of_price
from MercadoControl_Backend.products.models import Product


def scrape_view(request):
    data = obtener_jumbo('https://www.tiendasjumbo.co/supermercado/despensa')
    crear_producto(data.get('productos'))
    return render(request, 'template.html', data)

def obtener_jumbo(url):
    units = (
        ("Kg", "Kg"),
        ("kg", "Kg"),
        ("Lb", "Lb"),
        ("lb", "Lb"),
        ("g", "g"),
        ("G", "g"),
        ("L", "L"),
        ("l", "L"),
        ("ML", "mL"),
        ("mL", "mL"),
        ("und", "Unidad"),
    )

    # Configura Selenium con el controlador de Chrome
    service = Service('ruta/al/controlador/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Emula un scroll down para cargar más productos
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Espera a que se cargue la página y obtiene su código HTML
    time.sleep(10)
    html = driver.page_source

    # Cierra el navegador
    driver.quit()

    # Crea un objeto BeautifulSoup con el código HTML obtenido
    soup = BeautifulSoup(html, 'html.parser')

    # Busca el div que contiene la clase 'render-container render-route-store-search-category'
    productos_div = soup.find_all('div',
                                  class_='vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--gallery-css vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--gallery-css--normal vtex-search-result-3-x-galleryItem--grid vtex-search-result-3-x-galleryItem--gallery-css--grid pa4')

    productos = list()

    for producto_div in productos_div:

        producto_temp_name = producto_div.find_all('span',
                                                   class_='vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body')
        producto_temp_price = producto_div.find_all('div', class_='tiendasjumboqaio-jumbo-minicart-2-x-price')
        if producto_temp_name != [] and producto_temp_price != []:
            producto_temp_name = producto_temp_name[0].text
            producto_temp_price = producto_temp_price[0].text.replace('\xa0', ' ').replace('$', '').replace('.', '')
            producto_temp_und = producto_temp_name  .split(' ')
            producto_temp_und = producto_temp_und[len(producto_temp_und) - 2]
            for unit in units:
                if unit[0] in producto_temp_und:
                    producto_temp_und = unit[0]
            producto_temp = [producto_temp_name, producto_temp_price, producto_temp_und]
            productos.append(producto_temp)

        # producto_temp = [producto_temp_name, producto_temp_price]
        # productos.append(producto_temp)

    # Imprime el div encontrado
    for producto in productos:
        print("-", producto)

    print(len(productos))

    context = {
        'data': soup.prettify(),
        'productos':productos
    }

    return context

def crear_producto(productos):
    for producto in productos:
        product = Product.objects.get_or_create(
            name = producto[0],
            unit_of_measure = producto[2],
            amount = 1,
            category = 'ALACENA',
        )
        print(product)
        print(product.id)
        List_of_price.objects.get_or_create(
            price =int(producto[1]),
            supermarket_id = 10,
            product_id = product.id,
            brand = 1
        )
    return ''