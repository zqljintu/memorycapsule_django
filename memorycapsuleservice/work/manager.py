# 这是管理员部分
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework.settings import api_settings



@require_http_methods(["POST"])
def manage_main(request):
    if request.method == 'GET':
        return render(request, 'post.html')
    response = {}
    return JsonResponse(response)