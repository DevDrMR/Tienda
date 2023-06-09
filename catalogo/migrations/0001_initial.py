# Generated by Django 4.2 on 2023-04-12 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('razon_social', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=90)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Aquí usted va a escribir el nombre del proyecto', max_length=45)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('precio_unitario', models.FloatField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.proveedor')),
            ],
        ),
    ]
