from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static,serve
from django.conf import settings

from houselist.views import Reth

urlpatterns = [
	path('',Reth.as_view()),
	path('house/<int:id>/', Reth.as_view(),name='renih')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),]
