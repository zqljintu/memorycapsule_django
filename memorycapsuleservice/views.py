from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Capsule
from .models import User
from .utils import *
import logging


logger = logging.getLogger('log')

# Create your views here.
# 添加一项日记
@require_http_methods(["POST"])
def add_capsule(requset):
    if requset.method == 'GET':
        return render(requset, 'post.html')
    response = {}
    try:
        c_contet = requset.POST.get('capsule_content', '')
        c_id = requset.POST.get('capsule_id', '')
        c_type = requset.POST.get('capsule_type', '')
        c_time = requset.POST.get('capsule_time', '')
        c_date = requset.POST.get('capsule_date', '')
        c_location = requset.POST.get('capsule_location', '')
        c_person = requset.POST.get('capsule_person', '')
        c_image = requset.POST.get('capsule_image', '')
        if utils.checkStringEmpty(c_id):
            response['msg'] = 'add_error_namenull'
            response['error_name'] = 209
        else:
            capsule = Capsule()
            capsule.capsule_id = c_id
            capsule.capsule_type = c_type
            capsule.capsule_content = c_contet
            capsule.capsule_time = c_time
            capsule.capsule_date = c_date
            capsule.capsule_location = c_location
            capsule.capsule_image = c_image
            capsule.capsule_person = c_person
            capsule.save()
            response['msg'] = 'add_success'
            response['error_name'] = 206
    except Exception as e:
        response['msg'] = str(e)
        response['error_name'] = 1

    return JsonResponse(response)

# 拉取全部日记
@require_http_methods(["GET"])
def show_capsules(request):
    response = {}
    try:
        username = ''
        username = request.GET.get('username')
        if utils.checkStringEmpty(username):
            response['msg'] = str('usrtname_error')
            response['error_name'] = 205  # 账号错误
        else:
            capsules = Capsule.objects.all().filter(capsule_id=username).order_by('-id')
            response['list'] = json.loads(
                serializers.serialize("json", capsules))
            response['msg'] = 'success'
            response['error_name'] = 207
    except Exception as e:
        response['msg'] = str(e)
        response['error_name'] = 1

    return JsonResponse(response)

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
            if (len(User.objects.all().filter(user_name=username)) == 0 and (username != '')):
                user.user_name = username
                user.user_password = userpassword
                user.user_email = useremail
                user.user_sex = usersex
                user.save()
                response['msg'] = 'logup_success'
                response['error_name'] = 0
            else:
                response['msg'] = 'name_repeat'
                response['error_name'] = 201
        else:
            response['msg'] = 'name/password_error'
            response['error_name'] = 208
    except Exception as e:
        response['msg'] = str(e)
        response['error_name'] = 1

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
            response['error_name'] = 202  # 没有该账号
        else:
            if utils.checkTwoString(userpassword, User.objects.get(user_name=username).user_password):
                user = User.objects.get(user_name=username)
                response['msg'] = 'login_success'
                response['sex'] = user.user_sex
                response['error_name'] = 203  # 登录成功
            else:
                response['msg'] = 'login_error'
                response['error_name'] = 204  # 登录失败，账号密码不匹配
    except Exception as e:
        response['msg'] = str(e)
        response['error_name'] = 1

    return JsonResponse(response)


# 删除方法
@require_http_methods(["POST"])
def delete_capsule(requset):
    if requset.method == 'GET':
        return render(requset, 'post.html')
    response = {}
    try:
        username = requset.POST.get('username', '')
        capsulepk = requset.POST.get('capsulepk', '')
        if len(User.objects.all().filter(user_name=username)) == 0:
            response['msg'] = 'username_null'
            response['error_name'] = 202  # 没有该账号
        else:
            if len(Capsule.objects.all().filter(id=int(capsulepk))) != 0:
                capsule = Capsule()
                capsule = Capsule.objects.get(id=int(capsulepk))
                if capsule.capsule_id == username:
                    Capsule.objects.filter(id=capsulepk).delete()
                    response['msg'] = 'capsule_delete success'
                    response['error_name'] = 213  # 成功删除该条记录
                else:
                    response['msg'] = 'username is not id'
                    response['error_name'] = 212  # 该条记录不是该用户名创建
            else:
                response['msg'] = 'capsule_null'
                response['error_name'] = 211  # 没有该条记录
    except Exception as e:
        response['msg'] = str(e)
        response['error_name'] = 210  # 删除失败
    return JsonResponse(response)


# 修改方法
@require_http_methods(["POST"])
def edit_capsule(requset):
    if requset.method == 'GET':
        return render(requset, 'post.html')
    response = {}
    try:
        username = requset.POST.get('capsule_id', '')
        c_pk = requset.POST.get('capsule_pk', '')
        if len(User.objects.all().filter(user_name=username)) == 0:
            response['msg'] = 'username_null'
            response['error_name'] = 202  # 没有该账号
        else:
            if len(Capsule.objects.all().filter(id=int(c_pk))) != 0:
                c_contet = requset.POST.get('capsule_content', '')
                c_id = requset.POST.get('capsule_id', '')
                c_type = requset.POST.get('capsule_type', '')
                c_time = requset.POST.get('capsule_time', '')
                c_date = requset.POST.get('capsule_date', '')
                c_location = requset.POST.get('capsule_location', '')
                c_person = requset.POST.get('capsule_person', '')
                c_image = requset.POST.get('capsule_image', '')
                if utils.checkStringEmpty(c_id):
                    response['msg'] = 'eddit_error_namenull'
                    response['error_name'] = 209
                else:
                    capsule = Capsule.objects.get(id=int(c_pk))
                    capsule.capsule_id = c_id
                    capsule.capsule_type = c_type
                    capsule.capsule_content = c_contet
                    capsule.capsule_time = c_time
                    capsule.capsule_date = c_date
                    capsule.capsule_location = c_location
                    capsule.capsule_image = c_image
                    capsule.capsule_person = c_person
                    capsule.save()
                    response['msg'] = 'capsule_edit success'
                    response['error_name'] = 213  # 成功删除该条记录
            else:
                response['msg'] = 'capsule_null'
                response['error_name'] = 211  # 没有该条记录
    except Exception as e:
        response['msg'] = str(e)
        response['error_name'] = 215  # 修改失败
    return JsonResponse(response)
