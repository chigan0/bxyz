from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from grkm.models import Add
from datetime import datetime as da

#from pickle import dumps

# -*- coding: utf-8 -*-

class Test(TemplateView):
	template_name = 'str_content/base.html'

class Rend(TemplateView):
	def get(self,request):
		context = {"ad" : Add.objects.all()}
		return render(request,'str_content/objects_fills.html',context)
