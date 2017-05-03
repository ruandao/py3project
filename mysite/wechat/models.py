# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VAccount(models.Model):
    vName = models.CharField(max_length=30)
    vAccount = models.CharField(max_length=30)
    vQQ = models.CharField(max_length=30)
    category = models.CharField(max_length=250)
    area = models.CharField(max_length=30)
    tags = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    description = models.TextField()
    qrCode = models.ImageField(upload_to='uploads/qrCodes/')
    crawl_url = models.CharField(max_length=250)

class Blog(models.Model):
    account = models.ForeignKey(VAccount)
    title = models.CharField(max_length=250)
    content = models.TextField()
    recordTime = models.DateTimeField(auto_now_add=True)