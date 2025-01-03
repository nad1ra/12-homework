# Generated by Django 5.1.4 on 2024-12-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_description', models.CharField(max_length=20)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
    ]
