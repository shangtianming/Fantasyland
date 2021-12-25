from django.urls import path
from user.views import login,UserView,token_veri

app_name = "user"

urlpatterns = [
    path('login/', login),  # 代表请求接口路径
    path('all', UserView.as_view()),
    path('all<int:pk>', UserView.as_view()),
    path('token/', token_veri),  # 代表请求接口路径
]
