"""
用户数据序列化器
"""
from rest_framework import serializers
from api import models


class UserInfoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)

    class Meta:
        model = models.UserInfo
        exclude = ('created_tm', 'updated_tm', 'is_delete')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class UserTokenSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)

    class Meta:
        model = models.UserToken
        exclude = ('created_tm', 'updated_tm')


class ProjectListSerializer(serializers.ModelSerializer):
    # 在返回json中新增字段，数据源指向数据库字段
    create_time = serializers.DateTimeField(source="created_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)
    update_time = serializers.DateTimeField(source="updated_tm",
                                            format="%Y-%m-%d %H:%M:%S",
                                            required=False,
                                            read_only=True)

    class Meta:
        model = models.ProjectList
        # 映射全部字段
        # fields = '__all__'
        # 映射指定字段
        # fields = ('')
        # 排除字段
        exclude = ('created_tm', 'updated_tm', 'is_delete', 'pub_date')
