# cappuccino-server

Web Command Based File Server

This project, made with **Django** framework, aims to provide the user with an easy and free way to have access to their own files from anywhere in the world.

It provides developers with a basic system architecture to build their own server or client.
- Pluggable modules (contain each functionality)
- Client served as a web app (No dependencies with the Server, it can so be easily rebuilt on your own taste)
- API specification is the only connection between Server and Client
- Web based to maximize portability (no need of bringing the client software with you ... )

## Functionnalities

- File listing (table view)
- Copy
- Move
- Delete
- Download
- Upload
- Stream

## History

I wanted to have a customizable system to have access to my own files from outside home, but looking on the net I only found an old versioned django server or Server and Clients with too big dependencies to make the effort of rewriting my own client.

## Requirements

- a computer switched on
- connection to the net

## To do List:
------------------------------------------------------------
V check file download working properly
V multiple file upload
V hide upload form on specific command
V streaming video files
- responsive css
- define keyboard hotkeys
- mediacenter view
- progress bar for tracking download?
- possibility to choose upload destination directory
- extend possible command list
- verify commands are working (test.py in every module)
- write all the tests necessary
- include headers for code rating into readme.md
- defense against injection and risky commands
- check rights in command paths (.. syntax is risky)
V display server response
- commands history
- web ssh
- web torrent view
- relay a video download to the server -> stock into the drive
- fix elements size
- require login for video files (temporarily set them as static?)
- dynamically include modules urls
- make easy installing setup.py

## Requirements
See requirements.txt
mod_xsendfile (for apache2)
apache2 (installed and set up)

## Innovations

- [X] Download Delegation to Server of file / torrent
- [X] Encryption
- [X] Streaming
- [X] Easy to install and self-hosting
- [X] Filters and Handling of Multiple Files Selection (Download)
- [X] Shell
- [X] File Versioning with Git
