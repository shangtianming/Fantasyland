from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def index(request):
     # return HttpResponse('ok')
     return render(request, 'west_home.html')

from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail(request):
    book_list = Book.objects.order_by('pub_date')[:5]#查询数据不超过5条
    context = {'book_list': book_list}
    return render(request, 'detail.html', context)

def addBook(request):
    if request.method == 'POST':
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone#获取当前时间用
    temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()#保存数据

    #重定向
    return HttpResponseRedirect(reverse('detail'))

def delBook(request,book_id):
    bookid=book_id
    Book.objects.filter(id=bookid).delete()#删除数据
    return  HttpResponseRedirect(reverse('detail'))

import json
def jsonStandard(request):
    json_after=''
    if request.method=='POST':
        try:
            jsonname=request.POST['jsonname']
            json_before = json.loads(jsonname)
            json_after = json.dumps(json_before, indent=4, ensure_ascii=False)
        except Exception :
            json_after ="输入信息异常"
    context ={"jsonname":json_after}
    return render(request,'json.html',context)

