# Generated by Django 5.0.6 on 2024-12-07 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('OrderId', models.IntegerField()),
                ('GTIN', models.CharField(max_length=14, null=True)),
                ('BatchNumber', models.CharField(max_length=20, null=True)),
                ('ExpDate', models.CharField(max_length=10, null=True)),
                ('InsertDate', models.CharField(max_length=10, null=True)),
                ('LastXMLDate', models.CharField(max_length=10, null=True)),
                ('DistributerCompanyNid', models.CharField(max_length=11, null=True)),
                ('ProductionOrderId', models.CharField(max_length=20, null=True)),
                ('createdAt', models.DateTimeField(null=True)),
                ('updatedAt', models.DateTimeField(null=True)),
                ('DeviceId', models.CharField(max_length=20, null=True)),
                ('ordertype', models.CharField(max_length=20, null=True)),
                ('details', models.CharField(max_length=100, null=True)),
                ('userId', models.IntegerField(null=True)),
                ('documentCode', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'WarehouseOrders',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
        migrations.DeleteModel(
            name='WarehouseOrders',
        ),
        migrations.AlterModelOptions(
            name='whusers',
            options={'managed': False},
        ),
    ]
