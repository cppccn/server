# cappuccino-server

Web Command Based File Server

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
- python 2.7
- pip
- mysql
- virtualenv
- source

## Install
```bash
  git clone git@github.com:cappuccino-app/cappuccino-server.git
  cd cappuccino-server
  bash install.sh
```
While installing ...
- Put the password to clone git repositories
- Answer Yes to the Static files collection
- Insert your MySql Passwd in order for the script to create the database

In order to modify personal settings, edit owndrive/local_settings.py file, you can change the Shared Directory Path there (***/tmp*** by default), the Database used by Django, its name, user and password.

## Run
```bash
  bash run.sh
``` 
Navigate with your browser to http://localhost:8000 and login with ***admin_user*** as username using password you just set.

## Architecture
![alt tag](https://i.imgsafe.org/732f8bf199.jpg)

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
