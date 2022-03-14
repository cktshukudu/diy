from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('beauty/', views.beauty, name='beauty'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('medical/', views.medical, name='medical'),
    path('ngo/', views.ngo, name='ngo'),
    path('tourism/', views.tourism, name='tourism'),
]
