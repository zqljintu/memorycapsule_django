from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from rest_framework_jwt.utils import jwt_decode_handler

from memorycapsuleservice.model.models import Capsule
from memorycapsuleservice.model.models import User
import logging

from memorycapsuleservice.utils.utils import utils

logger = logging.getLogger('log')
"""
Created by jintu 2020/01/12
这是关于capsule操作的一些方法
"""


# Create your views here.
# 添加一项日记
@require_http_methods(["POST"])
def add_capsule(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        c_id = request.POST.get('username')
        c_contet = request.POST.get('capsule_content', '')
        c_type = request.POST.get('capsule_type', '')
        c_time = request.POST.get('capsule_time', '')
        c_date = request.POST.get('capsule_date', '')
        c_location = request.POST.get('capsule_location', '')
        c_person = request.POST.get('capsule_person', '')
        c_image = request.POST.get('capsule_image', '')
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
        username = request.GET.get('username')
        page = request.GET.get('page')
        if User.objects.all().filter(username=username).count() == 0:
            response['msg'] = str('username_null')
            response['code'] = 202  # 没有该账号
        else:
            capsules = Capsule.objects.all().filter(capsule_id=username).order_by('-id')
            paginator = Paginator(capsules, 20)
            try:
                result = paginator.page(page)
            except PageNotAnInteger:
                result = paginator.page(1)
            except InvalidPage:
                result = 'not fond any page'
            except EmptyPage:
                result = paginator.page(paginator.num_pages)
            response['list'] = json.loads(
                serializers.serialize("json", result))
            response['page'] = page
            response['pagecount'] = paginator.num_pages
            response['msg'] = 'success'
            response['code'] = 207
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


# 删除方法
@require_http_methods(["POST"])
def delete_capsule(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        capsulepk = request.POST.get('capsule_pk', '')
        username = request.POST.get('username')
        if User.objects.all().filter(username=username).count() == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            if Capsule.objects.all().filter(id=int(capsulepk)).count() != 0:
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
def edit_capsule(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    try:
        c_pk = request.POST.get('capsule_pk', '')
        username = request.POST.get('username')
        if User.objects.all().filter(username=username).count() == 0:
            response['msg'] = 'username_null'
            response['code'] = 202  # 没有该账号
        else:
            if Capsule.objects.all().filter(id=int(c_pk)).count() != 0:
                c_content = request.POST.get('capsule_content', '')
                c_id = username
                c_type = request.POST.get('capsule_type', '')
                c_time = request.POST.get('capsule_time', '')
                c_date = request.POST.get('capsule_date', '')
                c_location = request.POST.get('capsule_location', '')
                c_person = request.POST.get('capsule_person', '')
                c_image = request.POST.get('capsule_image', '')
                if utils.checkStringEmpty(c_id):
                    response['msg'] = 'edit_usernull'
                    response['code'] = 209
                else:
                    capsule = Capsule.objects.get(id=int(c_pk))
                    capsule.capsule_id = c_id
                    capsule.capsule_type = c_type
                    capsule.capsule_content = c_content
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
        token = request.META.get('HTTP_AUTHORIZATION', '')
        logger.info('zzzzzzzzzzzzz-->%s', token)
        if utils.checkStringEmpty(token):
            response['msg'] = str('username_null')
            response['code'] = 221  # 账号为空
            return JsonResponse(response)
        else:
            user_dict = jwt_decode_handler(token=token)
            username = user_dict['username']
            if User.objects.all().filter(username=username).count() == 0:
                response['msg'] = str('username_null')
                response['code'] = 202  # 没有该账号
            else:
                size = Capsule.objects.all().filter(capsule_id=username).count()
                response['msg'] = str('capsulesize_success')
                response['size'] = size
                response['code'] = 222  # 获取capsule数量成功
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1
    return JsonResponse(response)
