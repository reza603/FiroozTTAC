# Generated by Django 5.0.6 on 2024-12-09 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0012_alter_inspection_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inspection',
            options={'managed': True},
        ),
    ]