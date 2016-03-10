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
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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
        return render(request, "apps/login/templates/login.html")