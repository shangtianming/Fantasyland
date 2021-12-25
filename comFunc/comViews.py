from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class ComAllAPIView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    GenericAPIView):

    # 查询
    def get(self, request, *args, **kwargs):
        if request.parser_context['kwargs']:  # 如果有id，则查单个值
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # 创建
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # 更新部分字段
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # 删除
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

