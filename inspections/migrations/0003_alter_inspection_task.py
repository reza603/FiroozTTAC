# Generated by Django 5.0.6 on 2024-12-01 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0002_alter_inspection_company_alter_inspection_referdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='task',
            field=models.CharField(max_length=50, verbose_name='عنون '),
        ),
    ]
