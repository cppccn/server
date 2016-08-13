from cappuccino import constants


class CommandFactory:

    def __init__(self):
        self.name = "factory"

    def createCommand(self, command):
        command_name = command.split(" ")[0]

        if command_name in constants.ALLOWED_COMMANDS:
            for entry in constants.ALLOWED_COMMANDS:
                if entry == command_name:
                    class_name = command_name[
                        0].capitalize() + command_name[1:] + "Command"
                    module = __import__("cappuccino.apps.command.modules." + class_name, globals(), locals(), [class_name], -1)
                    class_ = getattr(module, class_name)(command)
                    return class_
        else:
            return commands.ErrorCommand(command)
