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
            response['msg'] = 'add_codenull'
            response['code'] = 209
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
            response['code'] = 206
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)

# 拉取全部日记
@require_http_methods(["GET"])
def show_capsules(request):
    response = {}
    try:
        username = ''
        username = request.GET.get('username')
        logger.info('zzzzzzzzzzzzz%s-->', username)
        if utils.checkStringEmpty(username):
            response['msg'] = str('usrtname_error')
            response['code'] = 205  # 账号错误
        else:
            capsules = Capsule.objects.all().filter(capsule_id=username).order_by('-id')
            response['list'] = json.loads(
                serializers.serialize("json", capsules))
            response['msg'] = 'success'
            response['code'] = 207
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

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
            response['code'] = 202  # 没有该账号
        else:
            if len(Capsule.objects.all().filter(id=int(capsulepk))) != 0:
                capsule = Capsule()
                capsule = Capsule.objects.get(id=int(capsulepk))
                if capsule.capsule_id == username:
                    Capsule.objects.filter(id=capsulepk).delete()
                    response['msg'] = 'capsule_delete success'
                    response['code'] = 213  # 成功删除该条记录
                else:
                    response['msg'] = 'username is not id'
                    response['code'] = 212  # 该条记录不是该用户名创建
            else:
                response['msg'] = 'capsule_null'
                response['code'] = 211  # 没有该条记录
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 210  # 删除失败
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
            response['code'] = 202  # 没有该账号
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
                    response['msg'] = 'eddit_codenull'
                    response['code'] = 209
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
                    response['code'] = 213  # 成功修改该条记录
            else:
                response['msg'] = 'capsule_null'
                response['code'] = 211  # 没有该条记录
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 215  # 修改失败
    return JsonResponse(response)
