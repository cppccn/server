from django.conf.urls import url
from . import views
from cappuccino import settings

urlpatterns = []

if not settings.DEVELOPMENT_MODE:
    urlpatterns += [url(r'^$', views.FileView.as_view(), name='file_list')]
else:
    urlpatterns += [url(r'^$', views.FileViewDev.as_view(), name='file_list_dev')]