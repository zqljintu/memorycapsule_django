from django.conf.urls import url

from memorycapsuleservice.work import user, capsule

urlpatterns = [
    # 用户相关
    url(r'user_loginup', user.user_loginup, name="注册"),
    url(r"user_login", user.user_login, name="登录"),
    url(r"user_logout$", user.user_logout, name="注销"),
    url(r"edit_nickname$", user.edit_nickname, name="修改昵称"),
    url(r"edit_usertitle$", user.edit_usertitle, name="修改个性签名"),
    # 业务相关
    url(r'add_capsule$', capsule.add_capsule, name="添加日记"),
    url(r'show_capsules$', capsule.show_capsules, name="拉取日记"),
    url(r"delete_capsule", capsule.delete_capsule, name="删除"),
    url(r"edit_capsule", capsule.edit_capsule, name="修改"),
    url(r"size_capsule$", capsule.get_capsuleSize, name="获取日记条数")
]
