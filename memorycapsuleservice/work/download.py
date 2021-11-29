
# 下载apk程序
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from memorycapsuleservice.utils.utils import utils


@require_http_methods(["GET"])
def download_file(request):
    # do something
    try:
        the_file_name = request.GET.get('filename', "")  # 显示在弹出对话框中的默认的下载文件名
        filename = 'vue_work/dist/static/media/userimage/' + the_file_name  # 要下载的文件路径
        response = StreamingHttpResponse(readFile(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1
    return response


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


# 检测有没有最新版本程序
@require_http_methods(["GET"])
def checkVersion_apk(request):
    # 检测目前是否要更
    response = {}
    try:
        the_file_name = request.GET.get('filename', "")  # 显示在弹出对话框中的默认的下载文件名
        filename = 'vue_work/dist/static/media/userimage/' + the_file_name  # 要下载的文件路径
        response['code'] = 0  # 账号为空
        response['md5'] = utils.md5(filename)
        response['url'] = str("http://" + "172.16.10.197:8000" + "/api/download_apk?=&filename=" + the_file_name)
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1
    return JsonResponse(response)
