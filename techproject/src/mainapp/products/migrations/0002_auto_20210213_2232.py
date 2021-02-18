# Generated by Django 3.1.6 on 2021-02-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Appetizers', 'Appetizers'), ('Entrees', 'Entrees'), ('Treats', 'Treats'), ('Drinks', 'Drinks')], max_length=60),
        ),
    ]