# Generated by Django 5.0.6 on 2024-12-19 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0023_alter_inspection_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspection',
            name='referdate',
        ),
    ]
