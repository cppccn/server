from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.FileView.as_view(), name='file_list'),
]