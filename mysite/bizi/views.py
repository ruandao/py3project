from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Category, Img
# Create your views here.
def index(request):
    categorys = Category.objects.all()
    imgs = Img.objects.all().order_by('-pub_date')[:15]
    return render(request, 'bizi/index.html', {
        'categorys': categorys,
        'images': imgs
    })

def category(request, cate_id):
    return render(request, 'bizi/category.html', {})

def getImg(request, img_id):
    return render(request, 'bizi/image.html', {})

def upload(request):
    return render(request, 'bizi/upload.html', {})
