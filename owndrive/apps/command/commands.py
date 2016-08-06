from BaseCommand import BaseCommand
from owndrive import constants
from os import listdir
from os.path import isfile, join
from owndrive.apps.command.tools.FileEntry import *
import shlex, subprocess

baseDir = constants.SHARED_PATH + "/"

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