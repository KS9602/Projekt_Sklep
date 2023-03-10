# Generated by Django 4.1.7 on 2023-03-06 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_shop', '0021_rename_avilable_advertisement_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('0', 'Gotowka'), ('1', 'Blik'), ('2', 'Przelew')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shopuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='super_shop.shopuser'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('0', 'Nowy'), ('1', 'Używany')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(choices=[('0', 'Sport'), ('1', 'Dom'), ('2', 'Elektronika'), ('3', 'Uroda'), ('4', 'Rozrywka'), ('5', 'Odzież'), ('6', 'Motoryzacja')], max_length=40, null=True),
        ),
    ]
