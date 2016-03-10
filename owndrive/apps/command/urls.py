from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^command/$', views.CommandView.as_view(), name='command'),
]