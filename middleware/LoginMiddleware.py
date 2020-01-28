import jwt
from django.utils.deprecation import MiddlewareMixin
from memorycapsuleservice.model.models import User

from django.http import HttpResponse, JsonResponse
from rest_framework_jwt.utils import jwt_decode_handler
from memorycapsuleservice.utils.utils import utils


class LoginMiddleware(MiddlewareMixin):
    # request请求时执行
    def process_request(self, request):
        response = {}
        need_token = ['/api/user_logout', '/api/add_capsule', '/api/show_capsules', '/api/delete_capsule',
                      '/api/edit_capsule', '/api/size_capsule', '/api/edit_nickname', '/api/edit_usertitle']
        if request.path not in need_token:
            pass
        else:
            try:
                token = request.META.get('HTTP_AUTHORIZATION', '')
                if utils.checkStringEmpty(token):
                    response['msg'] = str('username_null')
                    response['code'] = 221  # 账号为空
                    return JsonResponse(response)
            except AttributeError:
                response['msg'] = str('Token null')
                response['code'] = 221  # token为空
                return JsonResponse(response)
            try:
                user_dict = jwt_decode_handler(token=token)
                username = user_dict['username']
                if request.method == 'GET':
                    data = request.GET.copy()
                    data["username"] = username
                    request.GET = data
                else:
                    data = request.POST.copy()
                    data["username"] = username
                    request.POST = data
                print("zzzzzz----->", data)
            except jwt.ExpiredSignatureError:
                response['msg'] = str('Token expired')
                response['code'] = 221  # token已过期
                return JsonResponse(response)
            except jwt.InvalidTokenError as e:
                response['msg'] = str(e)
                response['code'] = 221  # token无效
                return JsonResponse(response)
            except Exception as e:
                response['msg'] = str('UserObject can not got')
                response['code'] = 221  # token无效
                return JsonResponse(response)

    # response返回过程执行
    def process_response(self, request, response):
        return response
