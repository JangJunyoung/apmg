# coding: utf-8
from django.db import models

# Create your models here.
class Spec(models.Model):
    name = models.CharField(max_length=100)

class Charge(models.Model):
    name = models.CharField(max_length=100)
    at = models.DateTimeField(verbose_name=u'날짜')

class UnpaidCharge(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(verbose_name=u'금액')
    at = models.DateTimeField(verbose_name=u'날짜')    
