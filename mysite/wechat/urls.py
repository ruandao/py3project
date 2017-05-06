from django.conf.urls import url

from  . import views

app_name = 'wechat'
urlpatterns = [
    url(r'^alluser/(?P<curPage>[0-9]+)/$', views.index, name='alluser'),
    url(r'^user/(?P<userid>[^/]+)/$', views.userPage, name="userPage"),
]