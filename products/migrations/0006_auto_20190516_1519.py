# Generated by Django 2.0.13 on 2019-05-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190516_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageAlt',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productDescript',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='productGenre',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women')], default='draft', max_length=50),
        ),
    ]
