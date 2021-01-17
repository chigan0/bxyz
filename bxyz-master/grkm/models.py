from django.db import models

class Add(models.Model):
	addr = models.CharField('Улица',unique=True,max_length=86,blank=False,default=None)

	def __str__(self):
		return self.addr
