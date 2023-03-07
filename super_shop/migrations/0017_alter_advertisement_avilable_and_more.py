# Generated by Django 4.1.7 on 2023-02-28 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0016_alter_productimg_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='avilable',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Czy ogloszenie ma byc aktywne'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description_adv',
            field=models.TextField(blank=True, null=True, verbose_name='Tresc ogloszenia: '),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='super_shop.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
