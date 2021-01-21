from django.db import models
from grkm.models import Add
from django.utils import timezone
from django.contrib.auth.models import User

class Apartments(models.Model):
	fr,fif = 'Покупка','Аренда'
	b,t,k = 'Битон','Кирпич','Саман'
	x,o = 'Да','Нет'

	cate = models.ForeignKey(Add,verbose_name='Улица',default=None,on_delete=models.CASCADE)
	name = models.CharField('Титул объекта',max_length=150,blank=True)
	
	square = models.IntegerField('Общая площадь',default=7,blank=False)
	residential = models.IntegerField('Жилая площадь',blank=False,default=50)

	roomnumber = models.IntegerField('Количество Комнот',default=1)
	price = models.IntegerField('Цена',default=10000)
	kolrroom = models.IntegerField('Этажность дома',default=5)
	aparroom = models.IntegerField('На каком этаже дома',default=5)
	height = models.FloatField('Высота потолков',blank=False,default=3)
	ye = models.IntegerField('Год постройки объекта',blank=False,default=1970)
	gps = models.CharField('Адрес для Риэлтора',max_length=100,blank=False)
	opis = models.TextField('Описания объекта',max_length=500,blank=False,db_index=True,default="Отсутствует")
	number = models.CharField('Номер Риэлтора',max_length=100,blank=False,default='+77776907855')
	rename = models.ForeignKey(User, on_delete=models.CASCADE, null=True,)
	pub_date = models.DateField(default=timezone.now)
	typeOf = models.CharField(max_length=13,default='apartament')
	typ = models.CharField('Категория для объекта',max_length=20,choices=[(fr, 'Покупка'),(fif, 'Аренда')],default=fr)
	typwall = models.CharField('Материал стен',max_length=25,choices=[(b,'Битон'),(t,'Кирпич'),(k,'Саман')],default=b)
	pledge = models.CharField('Залог',max_length=25,choices=[(x,'Да'),(o,'Нет')],default=o)

	def __str__(self):
		return self.name

class Imah(models.Model):
	pid = models.ForeignKey(Apartments,default=None,related_name='img',on_delete=models.CASCADE)
	img = models.ImageField('Изоброжения объекта',upload_to='apartmentsimg',blank=False,db_index=True)