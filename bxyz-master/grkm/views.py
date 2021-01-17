def pimg(imgob,uf,i,rf):
	kk,joil = list(imgob.objects.filter(pid__exact=uf[i]['id']).values('img')),''
	if len(kk) != 0:
		joil = kk[0]['img']
	uf[i]['img'] = joil
	rf.append(uf[i])

def checkpr(request,uf,Imah,rf):
	for i in range(len(uf)):
		if int(uf[i]['price'])>int(request.POST.get('utt')) and int(uf[i]['price']) < int(request.POST.get('dutt')):
			pimg(Imah,uf,i,rf)