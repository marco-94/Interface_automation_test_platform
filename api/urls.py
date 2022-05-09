from django.urls import path
from django.conf.urls import include
from . import model_view_set
from rest_framework import routers


app_name = 'api'

router = routers.SimpleRouter()
router.register('user', model_view_set.UserListView, basename='')

urlpatterns = [
    path('', include(router.urls)),
]
