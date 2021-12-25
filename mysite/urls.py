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
from django.urls import path,include

from west.views import index, addBook, detail, delBook, jsonStandard
from fantasy.views import add, add2, index2, operationDB, form, investigate, getname, addname
from whitewall.views import project_del_update, project_get_add, interfaces_del_update, interfaces_get_add



urlpatterns = [
    # name：定义当前url的别名，允许在template中使用该别名来找到对应的url
    path('admin/', admin.site.urls),  # django管理员使用的（我自己设置的用户名是我名字拼音，密码是github的用户名）
    path('user/',  include('user.urls', namespace='user')),

    path('', index),  # http://127.0.0.1:8000/

    # 这三个仅仅是验证路径传参
    path('fantasy/index', index2, name='home'),  # http://127.0.0.1:8000/index
    path('fantasy/add', add, name='add'),  # http://127.0.0.1:8000/fantasy/add?a=8&b=8
    path('fantasy/add/<int:a>/<int:b>/', add2, name='add2'),  # http://127.0.0.1:8000/add/5/8/
    # 视图显示和请求处理
    path('fantasy/form', form, name='form'),
    path('fantasy/investigate', investigate, name='investigate'),
    path('fantasy/getname', getname, name='getname'),
    path('fantasy/addname', addname, name='addname'),
    path('fantasy/db', operationDB, name='db'),

    path('west/detail', detail, name='detail'),
    path('west/addBook/', addBook, name='addBook'),
    path('west/delBook/<int:book_id>/', delBook, name='delBook'),
    path('west/json', jsonStandard, name='jsonStandard'),

    path('white/projects/', project_get_add),  # 获取、添加
    path('white/projects/<int:id>/', project_del_update),  # 删除、修改
    path('white/interfaces/', interfaces_get_add),  # 获取、添加
    path('white/interfaces/<int:id>/', interfaces_del_update),  # 删除、修改
]
