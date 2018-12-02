import * as express from 'express';
import * as logger from 'morgan';
import * as bodyParser from 'body-parser';

const { lstatSync, readdirSync, readFile } = require('fs')
const { join } = require('path')

const ENCODING = 'utf8'
const errors = {
  PATH_NOT_FOUND: 'Requested path not found'
}

const isDirectory = source => {
  return new Promise((resolve, reject) => {
    try {
      resolve(lstatSync(source).isDirectory())
    } catch(err) {
      reject({ status: 404, err: errors.PATH_NOT_FOUND})
    }
  })
}

const getFileContent = source => {
  return new Promise((resolve, reject) => {
    readFile(source, ENCODING, function (err,data) {
      if (err) {
        reject(err)
      }

      resolve(data)
    });
  })
}

const getDirectoryContent = source => {
  return new Promise((resolve, reject) => {
    var content
    try {
      content = readdirSync(source)
      resolve(content.map(name => join(source, name)))
    } catch(err) {
      reject({ status: 404, msg: errors.PATH_NOT_FOUND })
    }
  })
}

// Creates and configures an ExpressJS web server
class App {

  // ref to Express instance
  public express: express.Application;

  //Run configuration methods on the Express instance.
  constructor() {
    this.express = express();
    this.middleware();
    this.routes();
  }

  // Configure Express middleware.
  private middleware(): void {
    this.express.use(logger('dev'));
    this.express.use(bodyParser.json());
    this.express.use(bodyParser.urlencoded({ extended: false }));
    this.express.use((req, res, next) => {
      res.header('Access-Control-Allow-Origin', '*');
      res.header('Access-Control-Allow-Headers',
                 'Origin, X-Requested-With, Content-Type, Accept');
      next();
    });
  }

  // Configure API endpoints.
  private routes(): void {
    /* This is just to get up and running, and to make sure what we've got is
     * working so far. This function will change when we start to add more
     * API endpoints */
    let router = express.Router();

    // placeholder route handler
    router.get('/*', (req, res, next) => {
      let path = `./${req.param('0') || ''}`

      isDirectory(path)
        .then(isdir => {
          if(isdir) {
            return getDirectoryContent(path)
              .then((result: Array<any>) => {
                let filePromise = (path) => isDirectory(path).then(isdir => new Object({ path: path, isDirectory: isdir }));
                return result.map(path => filePromise(path));
              }).then(result => Promise.all(result))
              .then(result => res.status(200).json(result))
              .catch(error => console.log('Error reading directory: ' + JSON.stringify(error)))
          } else {
            return getFileContent(path)
              .then(content => {
                res.header('Content-Type', 'text/plain')
                res.send(content)
              }).catch(err => console.log('Error reading file: ' + JSON.stringify(err)))
          }
        }).catch(err => this.onError(err, res))
    });
    this.express.use('/', router);
  }

  private onError(err, res) : void {
    res.status(err.status).json(err)
  }
}

export default new App().express;
