from BaseCommand import BaseCommand
from owndrive import constants
from os import listdir
from os.path import isfile, join
from owndrive.apps.command.tools.FileEntry import *
import shlex, subprocess

baseDir = constants.SHARED_PATH + "/"

class LsCommand(BaseCommand):
	def __init__(self, full_name):
		self.full_name = full_name

	def execute(self, currentDir):
		global baseDir
		currentDir = baseDir + currentDir
		print "EXECUTE : " + self.full_name
		if self.full_name != "ls":
			ls_path = self.full_name.split(" ")[1]
			if ls_path == "..":
				if currentDir != baseDir:
					hierarchy = currentDir.split("/")
					hierarchy.pop()
					hierarchy.pop()
					currentDir = "/".join(hierarchy)
					if not currentDir.endswith("/"):
						currentDir += "/"
			else:
				currentDir += ls_path
				if not currentDir.endswith("/"):
					currentDir += "/"

		# Check if path is allowed!
		print "Command : " + self.full_name
		print "Directory : " + currentDir


		file_list = []
		try:
			for entry in listdir(currentDir):
				file_entry = FileEntry(currentDir + "/" + entry)
				file_list.append(file_entry.toDict())
			response_dict = dict()
			i = 1
		except:
			return { "type" : "1", "message" : "Path not correct, file does not exist"}

		for entry in file_list:
			response_dict[i] = entry
			i += 1


		print response_dict
		return response_dict

class EasyCommand(BaseCommand):
	def __init__(self, full_name):
		self.full_name = full_name

	def execute(self, currentDir):
		args = shlex.split(self.full_name)
		proc = ""
		try:
			print "BEFORE PROC"
			proc = subprocess.check_output(self.full_name, stderr=subprocess.STDOUT, shell=True, cwd=constants.SHARED_PATH)
			print "PROC : " + proc
			# do something with output
		except subprocess.CalledProcessError:
			# There was an error - command exited with non-zero code
			return { "type" : 1, "message" : "-ERR: " + proc }
		
		return { "type" : 0, "message" : "+OK: " + proc}
		#p = subprocess.Popen(args) # Success!


class ErrorCommand(BaseCommand):
	def __init__(self, full_name):
		self.full_name = full_name

	def execute(self, currentDir):
		return {"type" : 0, "message" : "-ERR: command does not exist"}











