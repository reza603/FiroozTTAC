# Generated by Django 5.0.6 on 2024-12-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_accesslevel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseOrders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('OrderId', models.IntegerField(unique=True)),
                ('GTIN', models.CharField(blank=True, max_length=14, null=True)),
                ('BatchNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('ExpDate', models.CharField(blank=True, max_length=10, null=True)),
                ('InsertDate', models.CharField(blank=True, max_length=10, null=True)),
                ('LastXMLDate', models.CharField(blank=True, max_length=10, null=True)),
                ('DistributerCompanyNid', models.CharField(blank=True, max_length=11, null=True)),
                ('ProductionOrderId', models.CharField(blank=True, max_length=20, null=True)),
                ('createdAt', models.DateTimeField(blank=True, default=models.F('createdAt'), null=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=models.F('updatedAt'), null=True)),
                ('DeviceId', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('ordertype', models.CharField(blank=True, max_length=20, null=True)),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('userId', models.IntegerField(blank=True, null=True)),
                ('documentCode', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'WarehouseOrders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WhUsers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=255, null=True)),
                ('lname', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('createdAt', models.DateTimeField(blank=True, null=True)),
                ('updatedAt', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('company_nid', models.CharField(blank=True, max_length=12, null=True)),
                ('accepter_user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]