# Generated by Django 4.2.1 on 2023-07-10 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('barcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inquiryHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Code_type', models.CharField(choices=[('UUID', 'UUID'), ('RND', 'RndEsalat')], max_length=4)),
                ('cellphone', models.CharField(max_length=11)),
                ('datatime_created', models.DateTimeField(auto_now_add=True)),
                ('datatime_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=3, verbose_name=(('UUID', 'UUID'), ('RND', 'RndEsalat')))),
                ('Code_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barcode.barcode')),
                ('Customer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
