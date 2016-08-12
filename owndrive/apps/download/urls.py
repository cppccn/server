from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^download', views.DownloadView.as_view(), name='download'),
]
