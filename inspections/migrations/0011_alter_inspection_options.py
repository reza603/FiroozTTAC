# Generated by Django 5.0.6 on 2024-12-08 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0010_alter_inspection_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inspection',
            options={'managed': False},
        ),
    ]