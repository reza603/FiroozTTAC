# Generated by Django 5.0.6 on 2024-12-03 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiryHistory', '0004_scanlog_warehouseorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ScanLog',
        ),
        migrations.DeleteModel(
            name='WarehouseOrder',
        ),
    ]