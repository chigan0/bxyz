from django.utils import timezone
from django.db import models
from grkm.models import Add
from datetime import datetime
from django.contrib.auth.models import User

#Общая площадь,50 м² высота потолков тип строения кирпич
class House(models.Model):
	fr,fif = 'Покупка','Аренда'
	b,t,k = 'Битон','Кирпич','Саман'
	x,o = 'Да','Нет'

	cate = models.ForeignKey(Add,default=None,on_delete=models.CASCADE,verbose_name='Улица',blank=False)
	name = models.CharField('Титул объекта',max_length=150,blank=False)
	square = models.IntegerField('Общая площадь',default=7,blank=False)
	residential = models.IntegerField('Жилая площадь',blank=False,default=50)
	height = models.FloatField('Высота потолков',blank=False,default=3)
	roomnum = models.IntegerField('Количество этажей',default=1,blank=False)
	ye = models.IntegerField('Год постройки объекта',blank=False,default=1970)
	adrr = models.CharField('Точный Адрес для риэлтора',max_length=100,blank=False)
	roomnumber = models.IntegerField('Количество комнат',blank=False,default=1)
	opis = models.TextField('Описания',max_length=50000,default='Отсутствует',blank=False,db_index=True)
	price = models.IntegerField('Цена в Tг',default=3800000,blank=False)
	phonnum = models.CharField('Номер Риэлтора',max_length=15,blank=False,default='+77776907855')
	rename = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
	typeOf = models.CharField(max_length=8,default="house")
	pub_date = models.DateTimeField(default=timezone.now)
	typ = models.CharField('Категория для объекта',max_length=20,choices=[(fr, 'Покупка'),(fif, 'Аренда')],default=fr)
	typwall = models.CharField('Материал стен',max_length=25,choices=[(b,'Битон'),(t,'Кирпич'),(k,'Саман')],default=b)
	pledge = models.CharField('Залог',max_length=25,choices=[(x,'Да'),(o,'Нет')],default=o)

	def __str__(self):
		return self.name

class Imah(models.Model):
	pid = models.ForeignKey(House,default=None,related_name='img',on_delete=models.CASCADE)
	img = models.ImageField('Изоброжения объекта',upload_to="houseimg",blank=False,default='/static/houseimg/defa.jpg',db_index=True)