import os 
from PIL import Image

path = os.listdir(path=".")

fo = {'png':"PNG", "jpg":"JPEG", "jpeg":"JPEG","jfif":"JPEG"}

for i in range(len(path)):
	form = path[i].split('.')[-1]
	if form != 'py' and form != 'te':
		try:
			im = Image.open(path[i])
			im.save('te/'+path[i],format=fo[form],quality=50)
		except:
			print(form)
			print(path[i])
			continue
