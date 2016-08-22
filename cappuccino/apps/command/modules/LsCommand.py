from cappuccino.apps.command.models import BaseCommand
from cappuccino import constants
from os import listdir
from os.path import isfile, join
from cappuccino.apps.command.FileEntry import *
from cappuccino.apps.command.CommandResponse import *
import shlex
import subprocess

baseDir = constants.SHARED_PATH + "/"

class LsCommand(BaseCommand):

    def __init__(self, full_name):
        self.full_name = full_name

    def parentDir(currentDir, baseDir):
        if currentDir != baseDir:
            hierarchy = currentDir.split("/")
            hierarchy.pop()
            hierarchy.pop()
            currentDir = "/".join(hierarchy)
            if not currentDir.endswith("/"):
                currentDir += "/"

    def execute(self, currentDir):
        global baseDir
        currentDir = baseDir + currentDir

        """
        if self.full_name != "ls":
            ls_path = self.full_name.split(" ")[1]
            if ls_path == "..":
                self.parentDir(currentDir, baseDir)
            else:
                currentDir += ls_path
                if not currentDir.endswith("/"):
                    currentDir += "/"
        """
        # Check if path is allowed!
        print("Command : " + self.full_name)
        print("Directory : " + currentDir)

        # Sending a list of json FileEntry objects
        ls_result = []
        try:
            for entry in listdir(currentDir):
                file_entry = FileEntry(currentDir + "/" + entry)
                ls_result += [file_entry.toDict()]
        except:
            return CommandReponse(False, "Path not correct, file does not exist")

        return CommandResponse(True, ls_result)