"""
项目数据序筛选器
"""
import django_filters
from api import models


class ProjectListFilter(django_filters.rest_framework.FilterSet):
    project_id = django_filters.NumberFilter(field_name='project_id', lookup_expr='exact')
    project_name = django_filters.CharFilter(field_name='project_name', lookup_expr='icontains')
    project_description = django_filters.CharFilter(field_name='project_description', lookup_expr='icontains')

    class Meta:
        model = models.ProjectList
        fields = '__all__'
