
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import patterns, include, url
from rest_framework import routers
from owndrive.htmldrive import views
import htmldrive.views
from django.conf.urls.static import static
from owndrive import settings
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'files', views.FileView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^files/', include('htmldrive.urls'), namespace='htmldrive'),
    # url(r'^$', 'owndrive.views.home', name='home'),
    # url(r'^owndrive/', include('owndrive.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

#]

urlpatterns = [
    url(r'^$', include('owndrive.htmldrive.urls'), name='file-list'),
    url(r'^command/$', htmldrive.views.CommandView.as_view(), name='command'),
    url(r'^upload$', htmldrive.views.UploadView.as_view(), name='upload'),
    url(r'^download', htmldrive.views.DownloadView.as_view(), name='download'),
    #url(r'^users', htmldrive.views.UserViewSet, name='users'),
    #url(r'^groups', htmldrive.views.GroupViewSet, name='groups'),
    url(regex=r'^login/$', view=htmldrive.views.LoginView.as_view(), kwargs={'template_name': 'login.html'}, name='login'),
    url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/'}, name='logout'),
    #url(r'^$', htmldrive.views.LoginView.as_view(), name='file-list',),
    #url(r'^$', htmldrive.views.FileView.as_view(), name='file-list'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

