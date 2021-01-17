from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static,serve

from commercelist.views import test
from apartmentslist.views import getimg as g1
from houselist.views import getimg as g2

from .views import *
from .homer import Homer

urlpatterns = [
    path('admin/', admin.site.urls), #Админка 
    path('glav', Test.as_view(), name='glav'), # Главная страница
    path('', Test.as_view()), # Главная страница
    path("homer",Homer.as_view()), # Подгрузка всех обектов
    path('house', include('houselist.urls')), #Дома
    path('commerce', include('commercelist.urls')), #Комер обектый
    path('apartament', include('apartmentslist.urls')), # Апартаментый
    path('object',Rend.as_view(),name='reni'), # Страничка со всеми обектами
    
    path('apartament/get_img/<int:id>/',g1),#картинки для апартамента
    path('house/get_img/<int:id>/',g2),#картинки для апартамента
    
    path('house/<int:id>/', include("houselist.urls"), name = 'check_hous'), # страница с обявлениям House

    path('apartament/<int:id>/', include("apartmentslist.urls"), name='check_ape'), # страница с обявлениям apartamenst

    path('come/hoid/<int:id>/',test, name='check_comer'), # страница с обвлениям comerc
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),]
