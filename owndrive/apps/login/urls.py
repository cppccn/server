from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(regex=r'^login/$', view=views.LoginView.as_view(), name='login'),
    url(regex=r'^logout/$', view=logout,
        kwargs={'next_page': '/'}, name='logout'),
]
