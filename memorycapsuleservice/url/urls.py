from django.conf.urls import url

from memorycapsuleservice.work import user, capsule, manager, download

urlpatterns = [
    # 用户相关
    url(r'user_loginup', user.user_loginup, name="注册"),
    url(r"user_login", user.user_login, name="登录"),
    url(r"user_logout$", user.user_logout, name="注销"),
    url(r"edit_nickname$", user.edit_nickname, name="修改昵称"),
    url(r"edit_usertitle$", user.edit_usertitle, name="修改个性签名"),
    url(r"edit_userimg$", user.edit_userimg, name="修改用户头像"),
    url(r"user_info$", user.user_info, name="获取用户信息数据"),
    # 业务相关
    url(r'add_capsule$', capsule.add_capsule, name="添加日记"),
    url(r'show_capsules$', capsule.show_capsules, name="拉取日记"),
    url(r"delete_capsule", capsule.delete_capsule, name="删除"),
    url(r"edit_capsule", capsule.edit_capsule, name="修改"),
    url(r"size_capsule$", capsule.get_capsuleSize, name="获取日记条数"),
    # 管理相关
    url(r"manage_main", manager.manage_main, name="主方法"),
    #下载相关
    url(r'download_apk', download.download_file, name="下载文件"),
    url(r'checkversion_apk', download.checkVersion_apk, name="检测更新文件")
]
