from django.conf.urls import url
from .views import get_manage

urlpatterns = [
    url(r'^manage/', get_manage, name='manage'),
]