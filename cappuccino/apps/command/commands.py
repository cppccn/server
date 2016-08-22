from cappuccino import constants
from os import listdir
from os.path import isfile, join
from cappuccino.apps.command.FileEntry import *
import shlex
import subprocess

baseDir = constants.SHARED_PATH + "/"

class CommandParams:
    def __init__(self, command, currentDir):
        self.API_ENTRY_POINT = '/command/'
        self.command = command
        self.currentDir = currentDir

    def toDict(self):
        return { 'command': self.command, 'currentDir': self.currentDir }

class BaseCommand:
    def __init__(self, full_name):
        self.full_name = full_name

    def execute(self, currentDir):
        return None

class EasyCommand(BaseCommand):

    def __init__(self, full_name):
        self.full_name = full_name

    def execute(self, currentDir):
        args = shlex.split(self.full_name)
        proc = ""
        try:
            print("BEFORE PROC")
            proc = subprocess.check_output(
                self.full_name, stderr=subprocess.STDOUT, shell=True, cwd=constants.SHARED_PATH)
            print("PROC : " + proc)
            # do something with output
        except subprocess.CalledProcessError:
            # There was an error - command exited with non-zero code
            return {"type": 1, "message": "-ERR: " + proc}

        return {"type": 0, "message": "+OK: " + proc}
        # p = subprocess.Popen(args) # Success!
