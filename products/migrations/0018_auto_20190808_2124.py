# Generated by Django 2.2.3 on 2019-08-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20190808_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='products.Product'),
        ),
    ]
