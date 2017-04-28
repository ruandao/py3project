from django.conf.urls import url

from . import views

app_name = "bizi"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'category/(?P<cate_id>[0-9]*)/', views.category, name='category'),
    url(r'imgs/(?P<img_id>[0-9]*)/', views.getImg, name='img'),
    url(r'upload/', views.upload, name='upload'),
]
