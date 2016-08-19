from os import listdir
from os.path import isfile, join
import os
import time
from cappuccino import constants


class FileEntry:

    def __init__(self, path):
        self.path = path
        self.size = 0
        self.name = ""
        self.last_modified = ""
        self.build()

    def build(self):
        if isfile(self.path):
            self.type = "file"
            self.size = os.stat(self.path).st_size
        else:
            self.type = "dir"
            self.size = "0"

        self.last_modified = time.ctime(os.path.getmtime(self.path))
        self.name = self.path.split("/")[len(self.path.split("/")) - 1]

    def toDict(self):
        size = ""
        if(int(self.size) > 1024 * 1024):
            self.size = float(self.size) / (1024 * 1024)
            size = str(self.size) + " Mb"
        elif(int(self.size) > 1024):
            self.size = float(self.size) / 1024
            size = str(self.size) + " Kb"
        else:
            size = str(self.size) + " b"
        return {"name": self.name, "size": size, "last_modified": self.last_modified, "type": self.type}
