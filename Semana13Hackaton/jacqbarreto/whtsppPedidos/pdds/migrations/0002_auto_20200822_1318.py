# Generated by Django 3.1 on 2020-08-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='ubicacion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
