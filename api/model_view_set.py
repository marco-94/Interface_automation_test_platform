"""
自定义视图集
"""
from rest_framework import filters
from django_filters import rest_framework
from rest_framework import viewsets
from api import models
from .common.api_serializers import api_user_serializers
from .common.api_filters import api_user_filters, api_project_filters


class UserListView(viewsets.ModelViewSet):
    queryset = models.UserInfo.objects.filter(is_delete=0).all()
    serializer_class = api_user_serializers.UserInfoSerializer
    filter_class = api_user_filters.UserInfoFilter
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering = ['-created_tm']


class UserTokenView(viewsets.ModelViewSet):
    queryset = models.UserToken.objects.filter().all()
    serializer_class = api_user_serializers.UserTokenSerializer
    filter_class = api_user_filters.UserTokenFilter
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering = ['-created_tm']


class ProjectListView(viewsets.ModelViewSet):
    queryset = models.ProjectList.objects.filter().all()
    serializer_class = api_user_serializers.ProjectListSerializer
    filter_class = api_project_filters.ProjectListFilter
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering = ['-created_tm']
