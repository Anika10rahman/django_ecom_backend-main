# Generated by Django 4.1.4 on 2023-04-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inStock',
            field=models.BooleanField(default=False),
        ),
    ]
