from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('log/', views.log, name='log'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('medical/', views.medical, name='medical'),
    path('med/', views.med, name='med'),
    path('tourism/', views.tourism, name='tourism'),
    path('edu/', views.edu, name='edu'),
    path('clean/', views.clean, name='clean'),
    

]
