# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_users(request):
	#return HttpResponse("Hello client. How are you doing!!")
	#return "Hello client. How are you doing!!"
	return HttpResponse("<h1>Hello client. How are you doing!!</h1>")