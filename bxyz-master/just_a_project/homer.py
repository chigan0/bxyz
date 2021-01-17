from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from houselist.models import *
from apartmentslist.models import Apartments
from apartmentslist.models import Imah as jak
from django.views import View
from datetime import datetime
from threading import Thread
from grkm.views import pimg

class Homer(View):
	def get(self,request):
		joi = datetime.now()

		##################################################################
		arr=House.objects.values()
		arr1=Apartments.objects.values()
		res = []
		us1(arr,Imah,res)
		us1(arr1,jak,res)
		##################################################################
		print(datetime.now() - joi)

		return JsonResponse([res],safe=False,status=200)

def us1(a,img,res):
	for i in range(len(a)):
		pimg(img,a,i,res)