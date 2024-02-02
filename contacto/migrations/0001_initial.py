# Generated by Django 5.0.1 on 2024-02-02 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'consulta'), (1, 'sugerencia'), (2, 'enhorabuena')])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
                ('date', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]