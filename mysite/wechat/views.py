# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404


from .models import VAccount

# Create your views here.
def index(request, curPage=1):
    try:
        curPage = int(curPage)
    except:
        curPage = 1
    accounts = VAccount.objects.all()[(curPage - 1) * 20: curPage * 20]
    count = VAccount.objects.all().count()
    allPage = count / 20
    latestPage = allPage
    if allPage * 20 < count:
        latestPage = allPage + 1

    d = {}
    d["accounts"] = accounts
    d["curPage"] = curPage
    d["latestPage"] = latestPage
    if curPage != 1:
        d["prePage"]= curPage - 1
    if curPage != latestPage:
        d["nextPage"] = curPage + 1

    return render(request, 'wechat/index.html', d)

def userPage(request, userid, userName):
    account = get_object_or_404(VAccount, pk=userid)

    d = {}
    d['account'] = account
    return render(request, 'wechat/userPage.html', d)