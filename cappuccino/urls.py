
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from cappuccino import settings
from cappuccino import local_settings
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
import logging
import os

APPS_DIRECTORY = local_settings.PROJECT_ROOT + 'cappuccino/apps'

MODULES_INSTALLED = [module for module in os.listdir(APPS_DIRECTORY) if '.py' not in module and '__pycache__' not in module]

MODULES_URLS = [url(r'^', include('cappuccino.apps.' + module_name + '.urls')) for module_name in MODULES_INSTALLED]

urlpatterns = [
    # Comment the following line to disable the admin
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + MODULES_URLS