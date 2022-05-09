"""
用户数据序筛选器
"""
import django_filters
from api import models


class UserInfoFilter(django_filters.rest_framework.FilterSet):
    user_id = django_filters.NumberFilter(field_name='user_id', lookup_expr='exact')
    user_name = django_filters.CharFilter(field_name='user_name', lookup_expr='icontains')

    class Meta:
        model = models.UserInfo
        fields = '__all__'


class UserTokenFilter(django_filters.rest_framework.FilterSet):
    user_id = django_filters.NumberFilter(field_name='user_id', lookup_expr='exact')
    token = django_filters.CharFilter(field_name='token', lookup_expr='icontains')

    class Meta:
        model = models.UserToken
        fields = '__all__'
