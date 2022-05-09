from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .common.api_serializers import api_user_serializers
from api.utls import page_number


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