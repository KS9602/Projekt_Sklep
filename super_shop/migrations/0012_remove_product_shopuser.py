# Generated by Django 4.1.7 on 2023-02-26 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0011_alter_product_shopuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shopuser',
        ),
    ]