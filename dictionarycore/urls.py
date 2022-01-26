from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home',views.index,name='index'),
    path('search', views.search,name='search'),
    path('add_translation',views.addTranslation,name='add'),
    path('error',views.errorPage,name='error')
]