# Generated by Django 4.1.7 on 2023-02-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0006_product_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_product',
            field=models.TextField(null=True, verbose_name='Opis: '),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Nazwa produktu:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Cena:'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, default='default_item.jpg', null=True, upload_to='', verbose_name='Zdjecia'),
        ),
    ]