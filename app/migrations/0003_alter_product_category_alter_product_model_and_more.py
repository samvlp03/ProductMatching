# Generated by Django 5.0.7 on 2024-07-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='serial_no',
            field=models.CharField(max_length=255),
        ),
    ]
