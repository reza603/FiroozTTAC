# Generated by Django 4.2.1 on 2023-07-10 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inspections', '0001_initial'),
        ('InspectionDetails', '0001_initial'),
        ('barcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspectiondetail',
            name='Inspection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.inspection'),
        ),
        migrations.AddField(
            model_name='inspectiondetail',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='InspectionDetails.inspectiondetail'),
        ),
        migrations.AddField(
            model_name='inspectiondetail',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barcode.barcode'),
        ),
    ]
