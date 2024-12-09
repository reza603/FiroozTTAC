from django.db import models
class Company(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='Id', verbose_name='شناسه')
    internal_id = models.BigIntegerField(null=True, db_column='InternalID', verbose_name='شناسه داخلی')
    national_id = models.CharField(max_length=11, db_column='NationalId',unique=True, verbose_name='شناسه ملی')
    company_fa_name = models.CharField(max_length=128, null=True, db_column='CompanyFaName', verbose_name='نام شرکت (فارسی)')
    company_en_name = models.CharField(max_length=128, null=True, db_column='CompanyEnName', verbose_name='نام شرکت (انگلیسی)')
    insert_method = models.IntegerField(null=True, db_column='InsertMethod', verbose_name='روش درج')
    user_id = models.IntegerField(null=True, db_column='UserId', verbose_name='شناسه کاربر')
    insert_date = models.CharField(max_length=10, null=True, db_column='InsertDate', verbose_name='تاریخ درج')
    selected = models.BooleanField(null=True, db_column='Selected', verbose_name='انتخاب شده')
    default_dc = models.BooleanField(null=True, db_column='DefaultDC', verbose_name='DC پیشفرض')
    default_oc = models.BooleanField(null=True, db_column='DefaultOC', verbose_name='OC پیشفرض')
    prefix = models.IntegerField(null=True, db_column='Prefix', verbose_name='پیشوند')
    economic_id = models.CharField(max_length=20, null=True, db_column='EconomicId', verbose_name='شناسه اقتصادی')
    phone = models.CharField(max_length=15, null=True, db_column='Phone', verbose_name='تلفن')
    fax = models.CharField(max_length=15, null=True, db_column='Fax', verbose_name='فکس')
    reg_no = models.CharField(max_length=50, null=True, db_column='RegNo', verbose_name='شماره ثبت')
    address = models.CharField(max_length=255, null=True, db_column='Address', verbose_name='آدرس')
    postal_code = models.CharField(max_length=20, null=True, db_column='PostalCode', verbose_name='کد پستی')
    manager = models.CharField(max_length=100, null=True, db_column='Manager', verbose_name='مدیر')
    technical_assistant = models.CharField(max_length=100, null=True, db_column='TechnicalAssistant', verbose_name='دستیار فنی')
    order_assistant = models.CharField(max_length=100, null=True, db_column='OrderAssistant', verbose_name='دستیار سفارش')
    label_price = models.DecimalField(max_digits=18, decimal_places=0, null=True, db_column='LabelPrice', verbose_name='قیمت برچسب')
    setup_price = models.DecimalField(max_digits=18, decimal_places=0, null=True, db_column='SetUpPrice', verbose_name='قیمت راهاندازی')
    created_at = models.DateTimeField(null=True, db_column='createdAt', verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(null=True, db_column='updatedAt', verbose_name='تاریخ بهروزرسانی')
    invoice_prefix = models.CharField(max_length=10, null=True, db_column='InvoicePrefix', verbose_name='پیشوند فاکتور')
    class Meta:
        db_table = 'Companies'
        managed = False  # This ensures that Django does not try to manage the table's schema
    def __str__(self):
     result = self.company_fa_name or self.company_en_name or "Unnamed Company"
     print(f"Company __str__ called, returning: {result}")
     return result
     