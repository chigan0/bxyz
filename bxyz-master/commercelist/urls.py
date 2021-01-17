from django.contrib import admin
from django.urls import path

from commercelist.views import test

urlpatterns = [
	path('', test, name='comercli'),
]