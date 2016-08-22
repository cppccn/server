from cappuccino.apps.command.models import BaseCommand
from cappuccino import constants
from os import listdir
from os.path import isfile, join
from cappuccino.apps.command.FileEntry import *
from cappuccino.apps.command.CommandResponse import *
import shlex
import subprocess
from cappuccino import local_settings

class LsCommand(BaseCommand):
    def __init__(self, full_name):
        self.full_name = full_name

    def parentDir(self, currentDir):
        print("CurrentDir inside parentDir :  " + currentDir)
        if currentDir != local_settings.SHARED_PATH:
            hierarchy = currentDir.split("/")
            hierarchy.pop()
            hierarchy.pop()
            currentDir = "/".join(hierarchy)
            if not currentDir.endswith("/"):
                currentDir += "/"
        return None

    def execute(self, currentDir):
        """
        if self.full_name != "ls":
            ls_path = self.full_name.split(" ")[1]
            if ls_path == "..":
                self.parentDir(currentDir, local_settings.SHARED_PATH)
            else:
                currentDir += ls_path
                if not currentDir.endswith("/"):
                    currentDir += "/"
        """
        # Check if path is allowed!
        print("Command : " + self.full_name)
        print("Directory : " + currentDir)

        # Sending a list of json FileEntry objects
        return self.ls(currentDir)

    def ls(self, currentDir):
        if self.full_name == "ls": # Case no arguments
            path = local_settings.SHARED_PATH + currentDir
        else: # Case with arguments
            if self.full_name == "ls ..": # Case go back to parent
                parentDir = self.parentDir(currentDir)
                if parentDir:
                    path =  local_settings.SHARED_PATH + parentDir
                else:
                    path = local_settings.SHARED_PATH
            else: # Case ls path
                path = local_settings.SHARED_PATH + self.full_name.split(' ')[1]

        print("Ls System Path: " + path)
        ls_result = []
#        try:
        for entry in listdir(path):
            file_entry = FileEntry(path + "/" + entry)
            ls_result += [file_entry.toDict()]
#        except:
#            return CommandResponse(False, "Path not correct, file does not exist")

        print("Ls Results: " + ls_result.__str__())
        return CommandResponse(True, ls_result)