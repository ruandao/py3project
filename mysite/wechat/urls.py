from django.conf.urls import url

from  . import views

app_name = 'wechat'
urlpatterns = [
    url(r'^alluser/(?P<curPage>[0-9]+)/$', views.index, name='alluser'),
    url(r'^user/(?P<userid>[^/]+)/(?P<userName>[^/]+)/', views.userPage, name="userPage"),
    url(r'^blog/list/(?P<curPage>[0-9]+)/$', views.blogList, name='blogs'),
    url(r'^blog/(?P<blog_id>[0-9]+)/(?P<title>[^/]*)/', views.blogItem, name='blog'),
]