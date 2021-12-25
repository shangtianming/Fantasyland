from django.shortcuts import HttpResponse
import json
from .models import project, interfaces
from django.core.paginator import Paginator
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def project_get_add(request):
    data = json.loads(request.body)  # 获取请求数据
    if request.method == 'GET':
        # 获取项目数据
        page_num = data.get('page')
        size = data.get('size')
        results = project.objects.order_by('id')
        if results.exists():
            paginator = Paginator(results, size)  # 设置每页显示条数
            page = paginator.page(page_num)
        page = [i.to_dict() for i in page]
        result = {'results': page, 'count': len(results)}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    if request.method == 'POST':
        # 添加项目数据
        try:
            project.objects.create(**data)
            result = {'msg': '添加成功'}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=201)
        except Exception as e:
            result = {'msg': '添加失败', 'info': e}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=500)


# 请求的接口注意和url那边设置一致，因为发现请求的接口最后面少了/导致重定向到get
@api_view(['DELETE', 'PUT'])
@permission_classes((IsAuthenticated,))
def project_del_update(request, id):
    if request.method == 'DELETE':
        # 删除项目
        try:
            project.objects.filter(id=id).delete()
            result = {'msg': '删除成功'}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=204)
        except Exception as e:
            result = {'msg': '删除失败', 'info': e}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=500)
    if request.method == 'PUT':
        # 编辑项目
        try:
            data = json.loads(request.body)
            project.objects.filter(id=id).update(**data)
            result = {'msg': '编辑成功'}
            return HttpResponse(json.dumps(result, ensure_ascii=False))
        except Exception as e:
            result = {'msg': '编辑失败', 'info': e}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=500)


@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
def interfaces_get_add(request):
    data = json.loads(request.body)  # 获取请求数据
    if request.method == 'GET':
        # 获取接口数据
        page_num = data.get('page')
        size = data.get('size')
        results = interfaces.objects.order_by('id')
        if results.exists():
            paginator = Paginator(results, size)  # 设置每页显示条数
            page = paginator.page(page_num)
        page = [i.to_dict() for i in page]
        result = {'results': page, 'count': len(results)}
        return HttpResponse(json.dumps(result, ensure_ascii=False))
    if request.method == 'POST':
        # 添加接口数据
        try:
            interfaces.objects.create(**data)
            result = {'msg': '添加成功'}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=201)
        except Exception as e:
            result = {'msg': '添加失败', 'info': e}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=500)


@api_view(['DELETE', 'PUT'])
def interfaces_del_update(request, id):
    if request.method == 'DELETE':
        # 删除接口
        try:
            interfaces.objects.filter(id=id).delete()
            result = {'msg': '删除成功'}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=204)
        except Exception as e:
            result = {'msg': '删除失败', 'info': e}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=500)
    if request.method == 'PUT':
        # 编辑接口
        try:
            data = json.loads(request.body)
            interfaces.objects.filter(id=id).update(**data)
            result = {'msg': '编辑成功'}
            return HttpResponse(json.dumps(result, ensure_ascii=False))
        except Exception as e:
            result = {'msg': '编辑失败', 'info': e}
            return HttpResponse(json.dumps(result, ensure_ascii=False), status=500)
