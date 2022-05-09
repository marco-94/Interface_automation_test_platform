from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .common.api_serializers import api_user_serializers
from api.utls import page_number
import uuid


# Create your views here.
class UserView(APIView):
    def get_user_info(self, request):
        if request.method == 'GET':
            user_all = models.UserInfo.objects.all()
            user_list = page_number.PageNumber()
            user_obj = user_list.paginate_queryset(queryset=user_all, request=request, view=self)
            serializer = api_user_serializers.UserInfoSerializer(user_obj, many=True)
            return Response(serializer.data)

    @staticmethod
    def create_user(request, *args, **kwargs):
        if request.method == 'POST':
            serializer = api_user_serializers.UserInfoSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)


class LoginView(APIView):
    @staticmethod
    def login_in(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.UserInfo.objects.filter(user_name=username, password=password).first()
        print(user)
        if request.method == "POST":
            if user:
                token = uuid.uuid4()
                models.UserToken.objects.update_or_create(default={'token': token}, user=user)
                return Response({'code': 100, 'msg': '成功', 'token': token})
            else:
                return Response({'code': 101, 'msg': '失败，账号错误或密码错误'})