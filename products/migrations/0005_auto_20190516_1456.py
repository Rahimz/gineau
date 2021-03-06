# Generated by Django 2.0.13 on 2019-05-16 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='imageMain',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='products.Product'),
        ),
    ]
