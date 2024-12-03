
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
    migrations.CreateModel(
    name='Company',
    fields=[
    ('id', models.BigAutoField(primary_key=True, db_column='Id')),
    ('internal_id', models.BigIntegerField(null=True, db_column='InternalID')),
    ('national_id', models.CharField(max_length=11, db_column='NationalId')),
    ('company_fa_name', models.CharField(max_length=128, null=True, db_column='CompanyFaName')),
    ('company_en_name', models.CharField(max_length=128, null=True, db_column='CompanyEnName')),
    ('insert_method', models.IntegerField(null=True, db_column='InsertMethod')),
    ('user_id', models.IntegerField(null=True, db_column='UserId')),
    ('insert_date', models.CharField(max_length=10, null=True, db_column='InsertDate')),
    ('selected', models.BooleanField(null=True, db_column='Selected')),
    ('default_dc', models.BooleanField(null=True, db_column='DefaultDC')),
    ('default_oc', models.BooleanField(null=True, db_column='DefaultOC')),
    ('prefix', models.IntegerField(null=True, db_column='Prefix')),
    ('economic_id', models.CharField(max_length=20, null=True, db_column='EconomicId')),
    ('phone', models.CharField(max_length=15, null=True, db_column='Phone')),
    ('fax', models.CharField(max_length=15, null=True, db_column='Fax')),
    ('reg_no', models.CharField(max_length=50, null=True, db_column='RegNo')),
    ('address', models.CharField(max_length=255, null=True, db_column='Address')),
    ('postal_code', models.CharField(max_length=20, null=True, db_column='PostalCode')),
    ('manager', models.CharField(max_length=100, null=True, db_column='Manager')),
    ('technical_assistant', models.CharField(max_length=100, null=True, db_column='TechnicalAssistant')),
    ('order_assistant', models.CharField(max_length=100, null=True, db_column='OrderAssistant')),
    ('label_price', models.DecimalField(max_digits=18, decimal_places=0, null=True, db_column='LabelPrice')),
    ('setup_price', models.DecimalField(max_digits=18, decimal_places=0, null=True, db_column='SetUpPrice')),
    ('created_at', models.DateTimeField(null=True, db_column='createdAt')),
    ('updated_at', models.DateTimeField(null=True, db_column='updatedAt')),
    ('invoice_prefix', models.CharField(max_length=10, null=True, db_column='InvoicePrefix')),
    ],
    options={
    'db_table': 'Companies',
    'managed': False,
    },
    ),
    ]
