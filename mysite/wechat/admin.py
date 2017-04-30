# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import VAccount, Blog
# Register your models here.
admin.site.register(VAccount)
admin.site.register(Blog)