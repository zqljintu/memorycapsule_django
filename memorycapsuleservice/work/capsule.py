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
这是关于capsule操作的一些方法
"""


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
        username = request.GET.get('username', '')
        password = request.META.get('HTTP_PASSWORD', '')
        logger.info('zzzzzzzzzzzzz-->%s', username)
        logger.info('zzzzzzzzzzzzz-->%s', password)
        if utils.checkStringEmpty(password):
            response['msg'] = str('password_null')
            response['code'] = 220  # 密码为空
            return JsonResponse(response)
        if utils.checkStringEmpty(username):
            response['msg'] = str('username_null')
            response['code'] = 221  # 账号为空
            return JsonResponse(response)
        else:
            if User.objects.all().filter(user_name=username).count() == 0:
                response['msg'] = str('username_null')
                response['code'] = 202  # 没有该账号
            else:
                if utils.checkTwoString(password, User.objects.get(user_name=username).user_password):
                    capsules = Capsule.objects.all().filter(capsule_id=username).order_by('-id')
                    response['list'] = json.loads(
                        serializers.serialize("json", capsules))
                    response['msg'] = 'success'
                    response['code'] = 207
                else:
                    response['msg'] = str('name != pass')
                    response['code'] = 204  # 账号密码不匹配
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
        if User.objects.all().filter(user_name=username).count() == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            if Capsule.objects.all().filter(id=int(capsulepk)).count() != 0:
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
        if User.objects.all().filter(user_name=username).count() == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            if Capsule.objects.all().filter(id=int(c_pk)).count() != 0:
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


# 获取capsule数量方法
@require_http_methods(["GET"])
def get_capsuleSize(request):
    response = {}
    try:
        username = request.GET.get('username', '')
        password = request.META.get('HTTP_PASSWORD', '')
        logger.info('zzzzzzzzzzzzz-->%s', username)
        logger.info('zzzzzzzzzzzzz-->%s', password)
        if utils.checkStringEmpty(password):
            response['msg'] = str('password_null')
            response['code'] = 220  # 密码为空
            return JsonResponse(response)
        if utils.checkStringEmpty(username):
            response['msg'] = str('username_null')
            response['code'] = 221  # 账号为空
            return JsonResponse(response)
        else:
            if User.objects.all().filter(user_name=username).count() == 0:
                response['msg'] = str('username_null')
                response['code'] = 202  # 没有该账号
            else:
                if utils.checkTwoString(password, User.objects.get(user_name=username).user_password):
                    size = Capsule.objects.all().filter(capsule_id=username).count()
                    response['msg'] = str('capsulesize_success')
                    response['size'] = size
                    response['code'] = 222  # 获取capsule数量成功
                else:
                    response['msg'] = str('name != pass')
                    response['code'] = 204  # 账号密码不匹配
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1
    return JsonResponse(response)
