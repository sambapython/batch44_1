# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Customer

# Create your views here.
def view_users(request):
	#return HttpResponse("Hello client. How are you doing!!")
	#return "Hello client. How are you doing!!"
	return HttpResponse("<h1>Hello client. How are you doing!!</h1>")
def view_home(request):
	print request.method
	msg=""

	if request.method=="POST":
		data = {"name":request.POST.get("name"),
		"address": request.POST.get("address")}
		cust=Customer(**data)
		cust.save()
		msg="Customer created successfulyy"
		#import pdb; pdb.set_trace()
	data = Customer.objects.all()
	return render(request, "home.html",{"message":msg,"data":data})