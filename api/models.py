from django.db import models

# Create your models here.


class UserInfo(models.Model):
    # 用户基本信息表
    user_id = models.AutoField(help_text='用户ID', unique=True, primary_key=True)
    user_name = models.CharField(help_text='用户名称', max_length=128)
    user_icon = models.CharField(help_text='用户头像', null=True, max_length=128)
    nickname = models.CharField(help_text='用户昵称', null=True, max_length=128)
    password = models.CharField(help_text='用户密码', unique=True, max_length=128)
    is_delete = models.BooleanField(default=False, help_text='是否删除')
    updated_tm = models.DateTimeField(auto_now=True, help_text='更新时间')
    created_tm = models.DateTimeField(auto_now_add=True, help_text='创建时间')

    # 指定数据库表信息
    class Meta:
        db_table = 'user_info'
        verbose_name = '用户基本信息表'
        verbose_name_plural = verbose_name

    def delete(self, using=None, keep_parents=False):
        """重写数据库删除方法实现逻辑删除"""
        self.is_delete = True
        self.save()

    def __str__(self):
        return self.user_name


class UserToken(models.Model):
    # 用户登录信息表
    user = models.OneToOneField(to=UserInfo, on_delete=models.DO_NOTHING)
    token = models.CharField(help_text='token', max_length=128, default='')
    updated_tm = models.DateTimeField(auto_now=True, help_text='更新时间')
    created_tm = models.DateTimeField(auto_now_add=True, help_text='创建时间')

    # 指定数据库表信息
    class Meta:
        db_table = 'user_token'
        verbose_name = '用户登录信息表'
        verbose_name_plural = verbose_name


class ProjectList(models.Model):
    # 项目列表信息表
    project_id = models.AutoField(help_text='项目ID', unique=True, primary_key=True)
    project_name = models.CharField(help_text='项目名称', max_length=256)
    project_description = models.CharField(help_text='项目描述', max_length=1024)
    is_delete = models.BooleanField(default=False, help_text='是否删除')
    updated_tm = models.DateTimeField(auto_now=True, help_text='更新时间')
    created_tm = models.DateTimeField(auto_now_add=True, help_text='创建时间')

    # 指定数据库表信息
    class Meta:
        db_table = 'project_list'
        verbose_name = '项目列表信息表'
        verbose_name_plural = verbose_name

    def delete(self, using=None, keep_parents=False):
        """重写数据库删除方法实现逻辑删除"""
        self.is_delete = True
        self.save()
