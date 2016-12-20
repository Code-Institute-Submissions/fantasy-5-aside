from django.conf.urls import url
from .views import threads, new_thread, forum

urlpatterns = [
    url(r'^threads/(?P<subject_id>\d+)/$', threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', new_thread, name='new_thread'),
    url(r'^forum/$', forum, name='forum'),
]