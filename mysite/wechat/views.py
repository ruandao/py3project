# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import VAccount

# Create your views here.
def index(request):
    accounts = VAccount.objects.all()[:10]
    return render(request, 'wechat/index.html', {
        "accounts": accounts,
    })