from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<album_id>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='create_album'),
    # url(r'album/(?P<album_id>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update_album'),
    # url(r'album/(?P<album_id>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete_album'),
]
