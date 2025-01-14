# Generated by Django 4.2.1 on 2023-07-23 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0002_alter_company_address_alter_company_name_and_more'),
        ('inspections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='مکان مراجعه'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='referdate',
            field=models.DateTimeField(verbose_name='تاریخ مراجعه'),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='task',
            field=models.CharField(max_length=50, verbose_name='عنوان '),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='بازرس'),
        ),
    ]
