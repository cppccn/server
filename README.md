# CappuccinoServer

[![dependencies Status](https://david-dm.org/cppccn/server/status.svg)](https://david-dm.org/cppccn/server)
[![devDependencies Status](https://david-dm.org/cppccn/server/dev-status.svg)](https://david-dm.org/cppccn/server?type=dev)
[![Code Climate](https://img.shields.io/codeclimate/github/cppccn/server.svg)](https://codeclimate.com/github/cppccn/server)

## Motivations

This minimalist web server try to solve the issue of https://stackoverflow.com/questions/16333790/node-js-quick-file-server-static-files-over-http as alternate solution of the unmaintained https://github.com/indexzero/http-server but with the same API schema!

## Setup

```shell
$ npm install
$ gulp
$ npm start
```

## API Specifications

- Use the URL to specify the relative path between where `cppccn` command where launch and the file or the the folder you want to work on.

- Use `GET` to a folder to `ls -la` is content or to show/download (depends of the mimetype of the file and the capabilities of the browser) a text or binary file.

- Use `POST`, `DELETE`, `PUT`, etc... on a folder or a file to `cp`, `rm`, `mv`, etc...

Examples:

* `GET` http://localhost:3000/dist -> `ls` a directory
* `GET` http://localhost:3000/LICENSE -> download/show a text file
* `DELETE` http://localhost:3000/.gitignore -> `rm .gitignore`
