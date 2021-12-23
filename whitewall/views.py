from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        data=request.get_json()
        if data.get('username')=='whitewall' and data.get('password')=='12356':
            return  HttpResponse({'token':'token123456'})
        else:
            return HttpResponse({'token': 'token123456'},status=401)
