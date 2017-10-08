import * as express from 'express';
import * as logger from 'morgan';
import * as bodyParser from 'body-parser';

const { lstatSync, readdirSync } = require('fs')
const { join } = require('path')

const isDirectory = source => lstatSync(source).isDirectory()
const getDirectoryContent = source => {
  var content
  try {
    content = readdirSync(source)
    return Promise.resolve(content.map(name => join(source, name)))
  } catch(err) {
    return Promise.reject({ status: 404, msg: 'Required path not found' })
  }
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
      getDirectoryContent(`./${req.param('0') || ''}`)
        .then(result => {
          res.json(result.map(path => ({ path, isDirectory: isDirectory(path) })));
        }).catch(err => {
          this.onError(err, res);
        })
    });
    this.express.use('/', router);
  }

  private onError(err, res) : void {
    res.status(err.status).json(err)
  }
}

export default new App().express;
