from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:tid>', views.ticker, name= 'ticker'),#<str:tid>  str is looking for a string and assigns that value to tid
    path('graphs/', views.graphindex, name= 'graphindex'),
    path('graphs/<str:tid>/', views.graphticker, name='graphticker'),
]