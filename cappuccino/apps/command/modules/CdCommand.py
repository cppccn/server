from cappuccino.apps.command.models import BaseCommand
from cappuccino import constants
from os import listdir
from os.path import isfile, join
from cappuccino.apps.command.FileEntry import *
from cappuccino.apps.command.CommandResponse import *
import shlex
import subprocess
from cappuccino import local_settings

class CdCommand(BaseCommand):
    def __init__(self, full_name):
        self.full_name = full_name

    def execute(self, currentDir):
        # Sending a list of json FileEntry objects
        return self.cd(currentDir)

    # Returns a CommandResponse object with an ErrorMessage or the currentDir value after the command execution
    def cd(self, currentDir):
        if self.full_name == "cd .": # Case no arguments
            return CommandResponse(True, currentDir)
        elif self.full_name == "cd":
            return '/'
        else: # Case with arguments
            if self.full_name == "cd ..": # Case go back to parent
                parentDir = self.parentDir(currentDir)
                if parentDir:
                    path =  local_settings.SHARED_PATH + parentDir
                    return CommandResponse(True, path)
                else:
                    return CommandResponse(True, currentDir)
            else: # Case ls path
                return CommandResponse(True, local_settings.SHARED_PATH + self.full_name.split(' ')[1])

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