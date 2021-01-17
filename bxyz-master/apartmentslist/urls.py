from django.contrib import admin
from django.urls import path

from apartmentslist.views import ApartSend,getimg

urlpatterns = [
	path('', ApartSend.as_view(), name='apatli'),
	path('<int:id>',ApartSend.as_view(),name='rend'),
]