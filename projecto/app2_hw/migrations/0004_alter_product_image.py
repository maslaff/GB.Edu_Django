# Generated by Django 5.0.1 on 2024-01-31 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2_hw', '0003_remove_product_image_name_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='projecto/media/sunny.png', upload_to=''),
        ),
    ]