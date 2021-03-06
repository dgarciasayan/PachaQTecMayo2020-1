# Generated by Django 3.0.8 on 2020-07-26 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('almacen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ruc', models.IntegerField(default=99999999999)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correlativo', models.IntegerField(default=0)),
                ('fecha', models.DateField()),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cajero.Clientes')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='almacen.Producto')),
            ],
        ),
    ]
