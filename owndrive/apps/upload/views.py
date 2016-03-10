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
from owndrive.local_settings import *
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

class UploadView(View):
    def post(self, request, *args, **kwargs):
        def handle_uploaded_file(f):
            print "SHARED : " + SHARED_PATH
            with open(SHARED_PATH + "/" + f._name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

        print "Dentro upload view"
        print request.FILES.get('upl', 'nothing')
        handle_uploaded_file(request.FILES.get('upl[]', 'nothing'))

        response = HttpResponse("salut")
        return response