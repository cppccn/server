from django.conf.urls import url
from . import views
from cappuccino import settings

urlpatterns = []

if not settings.DEVELOPMENT_MODE:
    urlpatterns += [url(r'^command/$', views.CommandView.as_view(), name='command')]
else:
    urlpatterns += [url(r'^command/$', views.CommandViewDev.as_view(), name='command')]