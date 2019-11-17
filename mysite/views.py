from django.http import HttpResponse

def first_page(request):
    return HttpResponse("你好,世界！")