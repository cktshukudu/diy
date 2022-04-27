from django.urls import path
from . import views
from . import medi
from . import tourism

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('log/', views.log, name='log'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('medical/', medi.landing, name='medical'),
    path('medical/create/', medi.createWebString, name='send a creation form'),
    path('tourism/', tourism.landing, name='tourism'),
    path('tourism/create/', tourism.createWebString, name='send a creation form'),
    path('med/', views.med, name='med'),
    path('edu/', views.edu, name='edu'),
    path('clean/', views.clean, name='clean'),
    path('create/',views.createWebString,name='respond with choosen website'),
    path('create/',views.createWebString,name='respond with the form'),
    path('create/webfying/',views.create,name='create html content'),
    path('urls/<str:cName>/',medi.webSites,name='show different websites'),
]
