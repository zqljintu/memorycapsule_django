from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'add_capsule$', views.add_capsule, name="添加日记"),
    url(r'show_capsules$', views.show_capsules, name="拉取日记"),
    url(r'user_loginup', views.user_loginup, name="注册"),
    url(r"user_login", views.user_login, name="登录"),
    url(r"delete_capsule", views.delete_capsule, name="删除"),
    url(r"edit_capsule", views.edit_capsule, name="修改"),
    url(r"user_logout$", views.user_logout, name="注销")
]
