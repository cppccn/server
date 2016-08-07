from __future__ import print_function
import os
import logging
import string
import random

PROJECT_ROOT = os.getcwd() + '/'

log = logging.getLogger('ciao')
log.info(PROJECT_ROOT)

# Client-Web configuration, the server needs to know the paths in order to serve the client files
CLIENT_ROOT = PROJECT_ROOT + 'cappuccino-web/'
CLIENT_JS = CLIENT_ROOT + 'js'
CLIENT_CSS = CLIENT_ROOT + 'css'
CLIENT_APP = CLIENT_ROOT + 'app.html'

# Upload Form Configuration
UPLOAD_FORM_ROOT = CLIENT_ROOT + 'mini-upload-form/'
UPLOAD_FORM_JS = UPLOAD_FORM_ROOT + 'assets/js'
UPLOAD_FORM_CSS = UPLOAD_FORM_ROOT + 'assets/css'
UPLOAD_FORM_APP = UPLOAD_FORM_ROOT + 'index.html'

LOGIN_CSS = PROJECT_ROOT + 'owndrive/apps/login/css'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT + 'owndrive/static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    LOGIN_CSS,
    CLIENT_CSS,
    CLIENT_JS,
    UPLOAD_FORM_CSS,
    UPLOAD_FORM_JS,
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/tmp/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Make this unique, and don't share it with anybody.
# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

TEMPLATE_DIRS = (
    PROJECT_ROOT + 'owndrive/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cappuccino',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    }
}

LOGIN_URL = '/login/'

SHARED_PATH = "/tmp"
