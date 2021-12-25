from django.shortcuts import render
# Create your views here.
from django.shortcuts import HttpResponse
from fantasy.models import Character


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def index2(request):
    data = Character.objects.all()
    staff_str = list(map(lambda a: a.name, data))
    context = {}
    context['label'] = ' '.join(staff_str)
    return render(request, 'home.html', context)


# 视图显示和请求处理=============================================================
def form(request):
    return render(request, 'investigate.html')


def investigate(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)


from django.http import HttpResponseRedirect
from django.urls import reverse


def operationDB(request):
    # objects是是django默认的管理器对象，自己也可以在Character类下设置：objects=models.Manage()
    data = Character.objects.all()
    # staff_str = list(map(lambda a:a.name, data))
    # return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")
    return render(request, 'for.html', {"staffs": data})


def getname(request):
    alldata = Character.objects.all()
    return render(request, 'nameget.html', {"name": alldata})


def addname(request):
    if request.POST:
        newname = request.POST['staff']
    newdata = Character(name=newname)
    newdata.save()
    return HttpResponseRedirect(reverse('getname'))
