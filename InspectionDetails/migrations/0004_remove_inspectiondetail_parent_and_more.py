# Generated by Django 5.0.6 on 2024-12-19 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InspectionDetails', '0003_alter_inspectiondetail_scandatetime'),
        ('barcode', '0003_scanlog_delete_scanlogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspectiondetail',
            name='parent',
        ),
        migrations.AlterField(
            model_name='inspectiondetail',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='barcode.scanlog'),
        ),
    ]
