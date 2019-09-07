# Generated by Django 2.2.3 on 2019-09-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_product_productsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='products/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='products/image_thumb'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='products/image_thumb'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='products/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='products/image_thumb'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='products/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='products/image_thumb'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='products/image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='products/image_thumb'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.FileField(blank=True, null=True, upload_to='products/image'),
        ),
    ]
