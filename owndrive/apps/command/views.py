from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from owndrive.htmldrive.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import Context, Template
from owndrive import constants
from django.shortcuts import render_to_response
from django.template import loader
from django.http import JsonResponse
from owndrive.local_settings import *
from os import listdir
from os.path import isfile, join
import os, time
from owndrive.htmldrive.tools.commands import commands
from owndrive.htmldrive.tools.FileEntry import *
from owndrive.local_settings import *
import json
from owndrive.htmldrive.tools.commands.CommandFactory import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

currentDir = "/"
class CommandView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'

    def get(self, request, *args, **kwargs):
        global currentDir

        print "COMANDO: " + request.GET.get('command', 'ls')
        currentDir = request.GET.get('currentDir', '/')
        print "Current DIR : " + currentDir

        command = request.GET.get('command', 'ls')
        commandObject = CommandFactory().createCommand(command)
        response = commandObject.execute(currentDir + '/')

        return JsonResponse(response, safe="False")