# Generated by Django 4.2.3 on 2023-08-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='collection',
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(blank=True, to='products.collection'),
        ),
    ]
