from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='Id', verbose_name='شناسه')
    product_fr_name = models.CharField(max_length=128, null=True, db_column='ProductFrName', verbose_name='نام محصول (فارسی)')
    product_en_name = models.CharField(max_length=128, null=True, db_column='ProductEnName', verbose_name='نام محصول (انگلیسی)')
    old_irc = models.TextField(null=True, db_column='OldIRC', verbose_name='کد IRC قدیمی')
    irc = models.CharField(max_length=16, null=True, db_column='IRC', verbose_name='کد IRC')
    gtin = models.CharField(max_length=14, unique=True, db_column='GTIN', verbose_name='کد GTIN')
    producer_company_code = models.CharField(max_length=11, null=True, db_column='ProducerCompanyCode', verbose_name='کد شرکت تولید کننده')
    made_in_country = models.CharField(max_length=128, null=True, db_column='MadeInCountry', verbose_name='کشور سازنده')
    producer_company_name = models.CharField(max_length=128, null=True, db_column='ProducerCompanyName', verbose_name='نام شرکت تولید کننده')
    representitive = models.CharField(max_length=128, null=True, db_column='Representitive', verbose_name='نماینده')
    product_barcode = models.CharField(max_length=128, null=True, db_column='ProductBarcode', verbose_name='بارکد محصول')
    product_code = models.TextField(null=True, db_column='ProductCode', verbose_name='کد محصول')
    price = models.IntegerField(null=True, db_column='Price', verbose_name='قیمت')
    insert_method = models.IntegerField(null=True, db_column='InsertMethod', verbose_name='روش درج')
    user_id = models.IntegerField(null=True, db_column='UserId', verbose_name='شناسه کاربر')
    insert_date = models.CharField(max_length=10, null=True, db_column='InsertDate', verbose_name='تاریخ درج')
    brand = models.CharField(max_length=128, null=True, db_column='Brand', verbose_name='برند')
    beneficiary_company = models.CharField(max_length=128, null=True, db_column='BeneficiaryCompany', verbose_name='شرکت بهرهبردار')
    importer_company = models.CharField(max_length=128, null=True, db_column='ImporterCompany', verbose_name='شرکت وارد کننده')
    hs_code = models.CharField(max_length=50, null=True, db_column='HsCode', verbose_name='کد HS')
    info1 = models.TextField(null=True, db_column='Info1', verbose_name='اطلاعات 1')
    info2 = models.TextField(null=True, db_column='Info2', verbose_name='اطلاعات 2')
    website = models.TextField(null=True, db_column='WebSite', verbose_name='وبسایت')
    product_id = models.IntegerField(null=True, db_column='ProductId', verbose_name='شناسه محصول')
    pbarcode_id = models.IntegerField(null=True, db_column='PbarcodeId', verbose_name='شناسه بارکد')
    pcompany_id = models.IntegerField(null=True, db_column='Pcompanyid', verbose_name='شناسه شرکت')
    update_date = models.DateTimeField(null=True, db_column='UpdateDate', verbose_name='تاریخ بهروزرسانی')
    exp_days = models.IntegerField(null=True, db_column='ExpDays', verbose_name='روزهای انقضا')
    created_at = models.DateTimeField(null=True, db_column='createdAt', verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(null=True, db_column='updatedAt', verbose_name='تاریخ بهروزرسانی')
    factory_price = models.IntegerField(default=0, db_column='FactoryPrice', verbose_name='قیمت کارخانه')

    class Meta:
      db_table = 'Products'
      managed = False  # This ensures that Django does not try to manage the table's schema

    def __str__(self):
        return self.product_en_name or self.product_fr_name