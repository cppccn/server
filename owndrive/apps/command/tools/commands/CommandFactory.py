from owndrive import constants
from owndrive.apps.command.tools.commands import commands

class CommandFactory:
	def __init__(self):
		self.name = "factory"

	def createCommand(self, command):
		command_name = command.split(" ")[0]
		if command_name in constants.ALLOWED_COMMANDS:
			if command_name == "ls":
				return commands.LsCommand(command)
			elif command_name == "cp":
				return commands.EasyCommand(command)
			elif command_name == "mv":
				return commands.EasyCommand(command)
			elif command_name == "rm":
				print "Remove Command"
		else:
			return commands.ErrorCommand(command)