# Generated by Django 5.0.6 on 2024-12-09 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_options'),
        ('inspections', '0013_alter_inspection_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='company',
            field=models.ForeignKey(db_column='NationalId', on_delete=django.db.models.deletion.CASCADE, to='companies.company', to_field='national_id', verbose_name='مکان مراجعه'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='task',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
    ]
