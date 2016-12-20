from django.conf.urls import url
from .views import register, login, logout, get_csv

urlpatterns = [
    url(r'^register$', register, name='register'),
    url(r'^logout$', logout, name='logout'),
    url(r'^login$', login, name='login'),
    url(r'^csv/$', get_csv),
]