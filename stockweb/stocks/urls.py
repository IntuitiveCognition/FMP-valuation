from django.urls import path

from . import views

urlpatterns = [
    path('<str:tid>', views.ticker, name= 'ticker'),#<str:tid>  str is looking for a string and assigns that value to tid
                                                       #this is how the page is named after the symbol entered
    path('', views.index, name='index'),
]