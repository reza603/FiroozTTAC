
from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    user = models.ForeignKey('account.customuser', on_delete=models.CASCADE)
    company = models.ForeignKey('companies.company', on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
    referraldate = models.DateField(null=True, blank=True)