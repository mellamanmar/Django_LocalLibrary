from django.urls import path
from .views import views
from . import templates


urlpatterns= [
    path('', views.index, name= 'index')
]