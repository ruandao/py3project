# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404


from .models import VAccount, Blog

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

def blogList(request, curPage):
    try:
        curPage = int(curPage)
    except:
        curPage = 1

    pageSize = 10
    blogs = Blog.objects.all()[(curPage - 1) * pageSize: curPage * pageSize]
    count = Blog.objects.all().count()
    allPage = count / pageSize
    latestPage = allPage
    if latestPage * pageSize < count:
        latestPage = latestPage + 1

    d = {}
    d["blogs"] = blogs
    d["curPage"] = curPage
    d["latestPage"] = latestPage
    if curPage != 1:
        d["prePage"] = curPage - 1
    if curPage != latestPage:
        d["nextPage"] = curPage + 1

    return render(request, "wechat/blogList.html", d)

def blogItem(request, blog_id, title):
    blog = get_object_or_404(Blog, pk=blog_id)

    d = {}
    d["blog"] = blog
    d["contents"] = blog.content.split("\n")

    return render(request, "wechat/blogItem.html", d)
