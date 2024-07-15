# Generated by Django 5.0.7 on 2024-07-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_product_serial_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScannedProduct1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=255)),
                ('serial_no', models.CharField(max_length=255)),
                ('part_no', models.CharField(max_length=255)),
                ('scanned_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ScannedProduct',
        ),
    ]
