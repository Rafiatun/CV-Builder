from . import views
from django.urls import path 
from .views import *


urlpatterns = [
    path('', views.Home , name="home"),
    path('makecv' , views.CVMaking , name="makecv"),
    path('info',views.InfoList , name="info"),
    path('getpdf/<int:id>/',views.Get_PDF , name="getpdf")
]