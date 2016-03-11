from owndrive.apps.command.models import BaseCommand

class ErrorCommand(BaseCommand):
	def __init__(self, full_name):
		self.full_name = full_name

	def execute(self, currentDir):
		return {"type" : 0, "message" : "-ERR: command does not exist"}