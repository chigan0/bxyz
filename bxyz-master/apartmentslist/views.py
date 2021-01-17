from grkm.views import pimg
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from grkm.models import Add
from .models import Apartments,Imah
from django.views.generic import TemplateView
from datetime import datetime

class ApartSend(TemplateView):
	#work with object House
	def post(self,request):
		jo = datetime.now()
		uf,rk,rf = None,[],[]
		if request.POST.get('addr') != 'False':
			ad = Add.objects.filter(addr__exact=request.POST.get('addr')).values('id')
			uf = Apartments.objects.filter(cate__exact=ad[0]['id']).values()
			if request.POST.get('type') != 'Все':
				uf = Apartments.objects.filter(cate__exact=ad[0]['id'],typ__exact=request.POST.get('type')).values()
		else:
			uf = Apartments.objects.all().values()
			if request.POST.get('type') != 'Все':
				uf = Apartments.objects.filter(typ__exact=request.POST.get('type')).values()
		
		
		########################################################################################
		if request.POST.get('utt') != 'False' and request.POST.get('dutt') != 'False':
			checkpr(request,uf,Imah,rf)
			print(datetime.now()-jo)
			return JsonResponse([rf],safe=False,status=200)
		########################################################################################	
		

		########################################################################################
		for i in range(len(uf)):
			pimg(Imah,uf,i,rf)
		print(datetime.now()-jo)
		return JsonResponse([rf],safe=False,status=200)
		########################################################################################

	#Find one object House by id
	def get(self,request,id):
		try:
			obj = Apartments.objects.get(id=id)
			context = {'dw' : obj}
			return render(request, 'str_content/obj_pages.html', context)
		
		except Exception as e:
			print(e)
			return render(request, 'notid.html')
#Find img by id
def getimg(request,id):
	a = list(Imah.objects.filter(pid__exact=id).values('img'))
	return JsonResponse(a,safe=False,status=200)
