# Generated by Django 5.0.6 on 2024-12-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0022_inspection_done_alter_inspection_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='done',
            field=models.BooleanField(default=False, verbose_name='status'),
        ),
    ]