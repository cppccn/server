# Pandoro

_HTTP API of filesystem_

Pandoro let you `GET` a [jtar](https://github.com/cppccn/jtar) archive of a given URL path and `POST` a [jsh](https://github.com/cppccn/jsh) of transactionnal commands.

## Core concept

The aims and purpose of Pandoro is to use filesystems abstractions are a common intermediate representation that allows developers to rapidly prototype and to easily switch between different database engines: FUSE drivers allow to mount a everything as a drive (e.g. [PostgreSQL](https://github.com/petere/postgresqlfs), [SSH](https://github.com/libfuse/sshfs), [WebDAV](https://wiki.archlinux.org/index.php/Davfs2), etc.)

In the future, we want to offer a complete CRUD REST API and support of GraphQL format would a nice bonus.
