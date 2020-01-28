from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from memorycapsuleservice.model.models import Capsule
from memorycapsuleservice.model.models import User
from rest_framework_jwt.settings import api_settings
import logging

from memorycapsuleservice.utils.utils import utils

logger = logging.getLogger('log')

"""
Created by jintu 2020/01/12
这是关于user操作的一些方法
"""


# Create your views here.

# 注册方法
@require_http_methods(["POST"])
def user_loginup(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        username = request.POST.get('username', '')
        userpassword = request.POST.get('password', '')
        useremail = request.POST.get('email', '')
        usersex = request.POST.get('sex', '')
        user = User()
        if len(username) != 0 and len(userpassword) != 0:
            if len(User.objects.all().filter(username=username)) == 0 and (username != ''):
                user.username = username
                user.userpassword = userpassword
                user.useremail = useremail
                user.usersex = usersex
                user.save()
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response['msg'] = 'logup_success'
                response['token'] = token
                response['sex'] = usersex
                if user.usertitle == '':
                    response['usertitle'] = '个性签名'
                else:
                    response['usertitle'] = user.usertitle
                if user.usernickname == '':
                    response['nickname'] = '昵称'
                else:
                    response['nickname'] = user.usernickname
                response['code'] = 0
            else:
                response['msg'] = 'name_repeat'
                response['code'] = 201
        else:
            response['msg'] = 'name/password_error'
            response['code'] = 208
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


# 注销账号方法
@require_http_methods(["POST"])
def user_logout(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        username = request.POST.get('username')
        password = request.POST.get('password', '')
        if len(username) != 0 and len(password) != 0:
            if len(User.objects.all().filter(username=username)) != 0 and (username != ''):
                user = User.objects.all().get(username=username)
                if user.userpassword == password:
                    user.delete()
                    capsules = Capsule.objects.all().filter(capsule_id=username)
                    for capsule in capsules:
                        capsule.delete()
                    response['msg'] = 'logout_success'
                    response['code'] = 219
                else:
                    response['msg'] = 'logout_error--> name!= pass'
                    response['code'] = 218
            else:
                response['msg'] = 'name null'
                response['code'] = 216
        else:
            response['msg'] = 'name/pass -->empty'
            response['code'] = 217
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


# 登录方法
@require_http_methods(["POST"])
def user_login(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        username = request.POST.get('username', '')
        userpassword = request.POST.get('password', '')
        if len(User.objects.all().filter(username=username)) == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            if utils.checkTwoString(userpassword, User.objects.get(username=username).userpassword):
                user = User.objects.get(username=username)
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response['token'] = token
                response['msg'] = 'login_success'
                response['sex'] = user.usersex
                if user.usertitle == '':
                    response['usertitle'] = '个性签名'
                else:
                    response['usertitle'] = user.usertitle
                if user.usernickname == '':
                    response['nickname'] = '昵称'
                else:
                    response['nickname'] = user.usernickname
                response['code'] = 203  # 登录成功
            else:
                response['msg'] = 'login_error'
                response['code'] = 204  # 登录失败，账号密码不匹配
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)

# 修改昵称
@require_http_methods(["POST"])
def edit_nickname(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        username = request.POST.get('username', '')
        nickname = request.POST.get('nickname', '')
        if len(User.objects.all().filter(username=username)) == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            user = User.objects.get(username=username)
            user.usernickname = nickname
            user.save()
            response['msg'] = 'edit_nickname success'
            response['code'] = 223
            response['nickname'] = user.usernickname
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


# 修改个性签名
@require_http_methods(["POST"])
def edit_usertitle(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        username = request.POST.get('username', '')
        usertitle = request.POST.get('usertitle', '')
        if len(User.objects.all().filter(username=username)) == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            user = User.objects.get(username=username)
            user.usertitle = usertitle
            user.save()
            response['msg'] = 'edit_usertitle success'
            response['code'] = 225
            response['usertitle'] = usertitle
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)
