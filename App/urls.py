from django.urls import path
from App.views import *

 
urlpatterns = [
    path("", inicio),
    path("listar_agenda/", agenda)
]