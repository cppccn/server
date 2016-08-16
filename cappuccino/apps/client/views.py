from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import Context, Template
from cappuccino import constants
from django.shortcuts import render_to_response
from django.template import loader
from django.http import JsonResponse
from cappuccino.local_settings import *
from os import listdir
from os.path import isfile, join
import os
import time
from cappuccino.local_settings import *
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class FileView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/'

    def get(self, request, *args, **kwargs):
        return HttpResponse(open(CLIENT_APP).read())