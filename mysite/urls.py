"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mysite.views import first_page
from west.views import index,addBook,detail,delBook,jsonStandard
from fantasy.views import add,add2,index2,operationDB,form,investigate,getname,addname
from whitewall.views import login

urlpatterns = [
    path('admin/', admin.site.urls),                #http://127.0.0.1:8000/admin/
    #path('', first_page),
    path('', index),                                #http://127.0.0.1:8000/
    path('add',add,name='add'),                     #http://127.0.0.1:8000/add?a=8&b=8
    path('add/<int:a>/<int:b>/',add2,name='add2'),  #http://127.0.0.1:8000/add/5/8/
    path('index', index2,name='home'),              #http://127.0.0.1:8000/index
    path('db', operationDB,name='db'),              #http://127.0.0.1:8000/db

    #视图显示和请求处理
    path('west/form', form,name='form'),            #http://127.0.0.1:8000/west/form
    path('west/investigate', investigate,name='investigate'),   # http://127.0.0.1:8000/west/investigate
    path('west/getname', getname,name='getname'),
    path('west/addname', addname,name='addname'),

    path('detail/', detail, name='detail'),
    path('addBook/', addBook, name='addBook'),
    path('delBook/<int:book_id>/', delBook, name='delBook'),

    path('json', jsonStandard, name='jsonStandard'),

    path('user/login/', login),
]

# from django.urls import reverse
# reverse('add2', args=(3,4))