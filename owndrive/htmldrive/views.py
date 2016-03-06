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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


from django.contrib.auth.mixins import LoginRequiredMixin
class FileView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'

    def get(self, request, *args, **kwargs):
        return HttpResponse(open(app_path).read())

class UploadView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(open(app_path2).read())

class LoginView(View):
    def post(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate
        user = authenticate(username=request.POST.get('username', 'none'), password=request.POST.get('password', 'none'))
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
            return HttpResponse("username and password incorrect")

    def get(self, request, *args, **kwargs):
        print "Get login request"
        return render(request, "htmldrive/templates/login.html")

currentDir = "/"
class CommandView(View):
    def get(self, request, *args, **kwargs):
        global currentDir

        print "COMANDO: " + request.GET.get('command', 'ls')
        currentDir = request.GET.get('currentDir', '/')
        print "Current DIR : " + currentDir

        command = request.GET.get('command', 'ls')
        commandObject = CommandFactory().createCommand(command)
        response = commandObject.execute(currentDir + '/')

        return JsonResponse(response, safe="False")

class DownloadView(View):
    def get(self, request, *args, **kwargs):
        global currentDir

        print "COMANDO: " + request.GET.get('command', 'ls')
        currentDir = request.GET.get('currentDir', '/')
        print "Current DIR : " + currentDir

        command = request.GET.get('command', 'ls')

        file_path = SHARED_PATH + '/' + command.split(" ")[1]
        print "FILE TO DOWNLOAD : " + file_path

        from django.utils.encoding import smart_str

        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(command.split(" ")[1])
        response['X-Sendfile'] = smart_str(file_path)
        # It's usually a good idea to set the 'Content-Length' header too.
        # You can also set any other required headers: Cache-Control, etc.
        return response

class UploadView(View):
    def post(self, request, *args, **kwargs):
        def handle_uploaded_file(f):
            print "SHARED : " + SHARED_PATH
            with open(SHARED_PATH + "/" + f._name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

        print "Dentro upload view"
        print request.FILES.get('upl', 'nothing')
        handle_uploaded_file(request.FILES.get('upl', 'nothing'))

        response = HttpResponse("salut")
        return response