# Generated by Django 3.2.18 on 2023-04-02 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('VERDURAS', 'VERDURAS'), ('CARNE', 'CARNE'), ('ASEO', 'ASEO'), ('ALACENA', 'ALACENA')], max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]