from django.shortcuts import HttpResponse
import json

# Create your views here.

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        if data.get('username')=='whitewall' and data.get('password')=='123456':
            result={'token':'token123456','msg':'登录成功'}
            return  HttpResponse(json.dumps(result,ensure_ascii=False))
        else:
            result = {'msg': '账号密码不正确'}
            return HttpResponse(json.dumps(result),status=401)
