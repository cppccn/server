from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import Context, Template
from cappuccino import constants
from django.shortcuts import render_to_response
from django.template import loader
from django.http import JsonResponse
from cappuccino.local_settings import *
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from cappuccino import constants

currentDir = "/"

class CommandFactory:

    def __init__(self):
        self.name = "factory"

    def createCommand(self, command):
        command_name = command.split(" ")[0]

        if command_name in constants.ALLOWED_COMMANDS:
            for entry in constants.ALLOWED_COMMANDS:
                if entry == command_name:
                    class_name = command_name[0].capitalize() + command_name[1:] + "Command"
                    module = __import__("cappuccino.apps.command.modules." + class_name, globals(), locals(), [class_name], 0)
                    class_ = getattr(module, class_name)(command)
                    return class_
        else:
            return commands.ErrorCommand(command)


class CommandView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'

    def get(self, request, *args, **kwargs):
        global currentDir

        print("COMANDO: " + request.GET.get('command', 'ls'))
        currentDir = request.GET.get('currentDir', '/')
        print("Current DIR : " + currentDir)

        command = request.GET.get('command', 'ls')
        commandObject = CommandFactory().createCommand(command)
        response = commandObject.execute(currentDir + '/')

        return JsonResponse(response, safe="False")
