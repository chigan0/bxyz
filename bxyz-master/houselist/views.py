from grkm.views import *
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from grkm.models import Add,UserPng
from .models import House,Imah
from django.contrib import messages
from django.views import View
from datetime import datetime

class Reth(View):
	#work with object House
	def post(self,request):
		jo = datetime.now()
		####################################################################################
		self.uf,rf = None,[]
		if request.POST.get('addr') != 'False':
			ad = Add.objects.filter(addr__exact=request.POST.get('addr')).values('id')
			uf = House.objects.filter(cate__exact=ad[0]['id']).values()
			if request.POST.get('type') != 'Все':
				uf = House.objects.filter(cate__exact=ad[0]['id'],typ__exact=request.POST.get('type')).values()
		else:
			uf = House.objects.all().values()
			if request.POST.get('type') != 'Все':
				uf = House.objects.filter(typ__exact=request.POST.get('type')).values()
		
		##################################################################################
		if request.POST.get('utt') != 'False' and request.POST.get('dutt') != 'False':
			checkpr(request,uf,Imah,rf)
			print(datetime.now()-jo)
			return JsonResponse([rf],safe=False,status=200)
		##################################################################################

		########################################################################################
		for i in range(len(uf)):
			pimg(Imah,uf,i,rf)
		print(datetime.now()-jo)
		return JsonResponse([rf],safe=False,status=200)
		########################################################################################

	#Find one object House by id
	def get(self,request,id):
		try:
			houseid = House.objects.get(id=id)

			return render(request, 'str_content/obj_pages.html', context={
					'dw' : houseid,'img':UserPng.objects.filter(user=houseid.rename).values('img')[0]
				})
		except Exception as e:
			print(e)
			return render(request, 'notid.html')

#Find img by id
def getimg(request,id):
	a = list(Imah.objects.filter(pid__exact=id).values('img'))
	return JsonResponse(a,safe=False,status=200)
