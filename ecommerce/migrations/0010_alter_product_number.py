# Generated by Django 5.0.2 on 2024-06-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_product_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
