from django.contrib.auth.models import User

from django.db import models

class Add(models.Model):
	addr = models.CharField('Улица',unique=True,max_length=86,blank=False,default=None)

	def __str__(self):
		return self.addr

class UserPng(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)
	img = models.ImageField('Изоброжения объекта',upload_to='get_name',blank=False,db_index=True)

	def __str__(self):
		return self.user.username