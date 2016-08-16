# cappuccino-server

<img src="cappuccino.png" width="250" align="right">

[![Join the chat at https://gitter.im/cappuccino-app/cappuccino-server](https://badges.gitter.im/cappuccino-app/cappuccino-server.svg)](https://gitter.im/cappuccino-app/cappuccino-server?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/cappuccino-app/cappuccino-server.svg?branch=master)](https://travis-ci.org/cappuccino-app/cappuccino-server)

This project, made with **Django** framework, aims to provide the user with an easy and free way to have access to their own files from anywhere in the world, with no fees or storage limit, thanks to self-hosting.

It provides developers with a basic system architecture that can easily be extended:

- Pluggable modules (one par functionality)
- Client served as a web app
- No dependencies Client-Server, the API contract allows communication
- Web based to maximize portability (no need of bringing the client software with you ... )

## Requirements

- a computer switched on
- connection to the net
- read requirements.txt

### Set up for Prod

- mod_xsendfile (for apache2)
- apache2 (installed and set up)
- config ssl

### Set up for development purposes

- python2.7
- pip
- mysql
- virtualenv

## Default Automatic Install

```bash
  git clone git@github.com:cappuccino-app/cappuccino-server.git
  cd cappuccino-server
  bash install.sh
```

While installing ...

- Insert your MySQL passwd in order for the script to create the database
- Insert the password for the admin user automatically created

## Manual Installation

We'll start by installing virtualenv

```bash
pip install virtualenv
```

then we use the tool to create a virtual environment which will host all our django packages, then we activate it:

```bash
virtualenv env
source env/bin/activate
```

We download the Web-Client and move it inside the server main directory:

```bash
wget https://github.com/cappuccino-app/cappuccino-web/archive/master.zip
unzip master.zip
mv cappuccino-web-master cappuccino-web
```

We install all requirements using **_pip_**

```bash
# Python 2.7
pip install -r requirements2.7.txt
# Python 3.5
pip3 install -r requirements3.5.txt
```

We create a static files directory in order for our server to be able to collect and serve all static resources for login and the web-client:

```bash
mkdir -p cappuccino/static
python manage.py collectstatic --no-input
```

It's now the time to create a database for our server application, which we'll do by using mysql:

```bash
mysql -u [USERNAME] -e "CREATE DATABASE IF NOT EXISTS [DATABASE_NAME]"
```

We fill up **_local_settings.py_** with missing DATABASE informations:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '[DATABASE_NAME]', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '[DATABASE_USER]',
        'PASSWORD': '[DATABASE_PASSWD]',
        'HOST': 'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306', # Set to empty string for default.
    }
}
```

We apply all necessary database migration:

```bash
python manage.py migrate
```

Finally, we create a superuser in order to be able login through the Web-Client

```bash
python manage.py createsuperuser --username=admin_user --email=admin@cappuccino.com
```

In order to modify personal settings, edit `cappuccino/local_settings.py` file, you can change the Shared Directory Path there (`_/tmp_` by default), the Database used by Django, its name, user and password.

## Run

```bash
  bash run.sh
```

Navigate with your browser to <http://localhost:8000> and login with `admin_user` as username using password you just set.

## Functionnalities

- Web Interface
- Shell Commands (File System and Utilities)
- Download
- Upload
- Stream
- End-to-end Encryption
- Download Delegation to Server of file / torrent
- Easy to install and self-hosted
- Filters and Regex for searching Files
- File Versioning with Git

## History

I wanted to have a customizable system to have access to my own files from outside home, but looking on the net I only found an old versioned django server or Server and Clients with too big dependencies to make the effort of rewriting my own client.
