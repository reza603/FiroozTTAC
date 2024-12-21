import jdatetime

def datetime2jalali(gregorian_date):
    jalali_date = jdatetime.datetime.fromgregorian(datetime=gregorian_date)
    return jalali_date