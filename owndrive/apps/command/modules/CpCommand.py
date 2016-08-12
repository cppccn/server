from owndrive.apps.command.models import BaseCommand
from owndrive import constants
from os import listdir
from os.path import isfile, join
from owndrive.apps.command.FileEntry import *
import shlex
import subprocess

baseDir = constants.SHARED_PATH + "/"


class CpCommand(BaseCommand):

    def __init__(self, full_name):
        self.full_name = full_name

    def execute(self, currentDir):
        if not self.check():
            return {"type": 0, "message": "-ERR: " + "command not allowed"}

        args = shlex.split(self.full_name)
        proc = ""
        try:
            print "BEFORE PROC"
            proc = subprocess.check_output(
                args, stderr=subprocess.STDOUT, shell=True, cwd=constants.SHARED_PATH)
            print "PROC : " + proc
            # do something with output
        except subprocess.CalledProcessError:
            # There was an error - command exited with non-zero code
            return {"type": 1, "message": "-ERR: " + proc}

        return {"type": 0, "message": "+OK: " + proc}
        # p = subprocess.Popen(args) # Success!

    def check(self):
        if len(self.full_name.split(" ")) != 3:
            return False
        elif '\n' in self.full_name:
            return False
        return True
