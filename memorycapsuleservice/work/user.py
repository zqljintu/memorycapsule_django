from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from memorycapsuleservice.model.models import Capsule
from memorycapsuleservice.model.models import User
import logging

from memorycapsuleservice.utils.utils import utils

logger = logging.getLogger('log')

"""
Created bu jintu 2020/01/12
这是关于user操作的一些方法
"""
# Create your views here.

# 注册方法
@require_http_methods(["POST"])
def user_loginup(requset):
    if requset.method == 'GET':
        return render(requset, 'post.html')
    response = {}
    try:
        username = requset.POST.get('username', '')
        userpassword = requset.POST.get('password', '')
        useremail = requset.POST.get('email', '')
        usersex = requset.POST.get('sex', '')
        user = User()
        if len(username) != 0 and len(userpassword) != 0:
            if len(User.objects.all().filter(user_name=username)) == 0 and (username != ''):
                user.user_name = username
                user.user_password = userpassword
                user.user_email = useremail
                user.user_sex = usersex
                user.save()
                response['msg'] = 'logup_success'
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
def user_logout(requset):
    if requset.method == 'GET':
        return render(requset, 'post.html')
    response = {}
    try:
        username = requset.POST.get('username', '')
        password = requset.POST.get('password', '')
        logger.info('zzzzzzzzzzzzz1--->%s', username)
        logger.info('zzzzzzzzzzzzz2--->%s', password)
        if len(username) != 0 and len(password) != 0:
            if len(User.objects.all().filter(user_name=username)) != 0 and (username != ''):
                user = User.objects.all().get(user_name=username)
                if user.user_password == password:
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
def user_login(requset):
    if requset.method == 'GET':
        return render(requset, 'post.html')
    response = {}
    try:
        username = requset.POST.get('username', '')
        userpassword = requset.POST.get('password', '')
        user = User()
        if len(User.objects.all().filter(user_name=username)) == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            if utils.checkTwoString(userpassword, User.objects.get(user_name=username).user_password):
                user = User.objects.get(user_name=username)
                response['msg'] = 'login_success'
                response['sex'] = user.user_sex
                response['code'] = 203  # 登录成功
            else:
                response['msg'] = 'login_error'
                response['code'] = 204  # 登录失败，账号密码不匹配
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)
























