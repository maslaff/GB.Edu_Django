# Generated by Django 5.0.1 on 2024-01-31 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_hw', '0002_product_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_name',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
