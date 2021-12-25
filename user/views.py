from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password


@api_view(['POST'])  # 列表中的元素代表支持哪些请求方法
def login(request):
    """
    登录接口
    """
    # 验证用户帐号密码的内置方法
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if user:
        Token.objects.filter(user_id=user.id).delete()  # 删除原来的token
        token = Token.objects.create(user=user)  # 创建新的token
        return Response(data={'msg': '登录成功！', 'token': token.key})  # 返回登录信息及token
    return Response(data={'msg': '用户名或错误！'}, status=status.HTTP_401_UNAUTHORIZED)


from comFunc.comViews import ComAllAPIView
from user.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class UserView(ComAllAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        # 如果传递了password字段就用password的字段，没有则默认密码为123456
        pwd = request.data.get('password', '123456')
        request.data['password'] = make_password(pwd)  # 调用内置生成密码方法进行加密
        return self.create(request, *args, **kwargs)



