# Generated by Django 4.1.7 on 2023-02-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0005_alter_advertisement_description_adv'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, default='default_item.jpg', null=True, upload_to=''),
        ),
    ]
