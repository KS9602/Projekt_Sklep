# Generated by Django 4.1.7 on 2023-02-26 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0010_product_shopuser_alter_advertisement_avilable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shopuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='super_shop.shopuser'),
        ),
    ]