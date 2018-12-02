import { Constants } from './constants';
import * as ps from 'child_process';

const ALLOWED_COMMANDS = ['mv', 'cp'];
const SEPARATOR = ' ';

const contains = (container, contained) => {
  return container.indexOf(contained) >= 0 ? true : false;
}

export const isEnabled = command => {
  var err;
  if(!command) err = Constants.ERRORS.MISSING_CMD;
  else if(!contains(command, SEPARATOR)) err = Constants.ERRORS.CMD_MALFORMED;
  else {
    let split = command.split(SEPARATOR);
    let cmd = split && split.length ? split[0] : null;
    if(cmd && contains(ALLOWED_COMMANDS, cmd)) {
        if(split.length != 3) err = Constants.ERRORS.WRONG_ARGS_NUMBER;
        else return Promise.resolve();
    } else err = Constants.ERRORS.NOT_ALLOWED_CMD;
  }

  return Promise.reject(err);
}

export const execSh = command => {
  return new Promise((resolve, reject) => {
    ps.exec(command, (error, stdout, stderr) => {
        if (error) {
            console.log(`exec error: ${error}`);
            reject(error);
        } else resolve(stdout);
    });
  });
}

