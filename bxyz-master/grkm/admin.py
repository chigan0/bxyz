from django.contrib import admin
from .models import Add
from houselist.models import House
from houselist.models import Imah as on
from apartmentslist.models import Apartments,Imah
from grkm.models import UserPng

class InlineImah(admin.TabularInline):
	model = on

class Dar(admin.TabularInline):
	model = Imah

@admin.register(UserPng)
class UserPngAdmin(admin.ModelAdmin):
	pass

@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
	list_display = ('id','addr')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
	inlines = [InlineImah]
	exclude = ['typeOf','pub_date']
	list_display = ('id','name','pub_date','adrr')
	list_filter = ('pub_date','price','square','residential','height','roomnumber','ye')

@admin.register(Apartments)
class ApartmentsAdmin(admin.ModelAdmin):
	inlines = [Dar]
	exclude = ['typeOf','pub_date']
	list_display = ('id','name','pub_date','gps')
	list_filter = ('pub_date','price','roomnumber','square','cate','aparroom')
