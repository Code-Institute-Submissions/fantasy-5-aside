from django.conf.urls import url
from .views import get_leaderboard, profile, create_team, get_viewprofile, get_downloads, upload_csv, get_backup, change_team

urlpatterns = [
    url(r'leaderboard/', get_leaderboard, name='leaderboard'),
    url(r'profile/$', profile, name='profile'),
    url(r'createteam/', create_team, name='create_team'),
    url(r'(?P<id>\d+)/$', get_viewprofile, name='viewprofile'),
    url(r'downloads/', get_downloads, name='download_scorelist'),
    url(r'upload/', upload_csv, name='upload_scorelist'),
    url(r'backup/', get_backup),
    url(r'changeteam/', change_team, name='change_team'),
]