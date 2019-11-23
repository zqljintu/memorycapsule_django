from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'add_capsule$', views.add_capsule, name="添加日记"),
    url(r'show_capsules$', views.show_capsules, name="拉取日记"),
    url(r'user_loginup', views.user_loginup, name="注册"),
    url(r"user_login", views.user_login, name="登录"),

]
