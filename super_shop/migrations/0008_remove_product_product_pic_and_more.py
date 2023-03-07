# Generated by Django 4.1.7 on 2023-02-26 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0007_alter_product_description_product_alter_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_pic',
        ),
        migrations.AlterField(
            model_name='product',
            name='description_product',
            field=models.TextField(null=True, verbose_name='Opis:'),
        ),
        migrations.CreateModel(
            name='ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super_shop.product')),
            ],
        ),
    ]
