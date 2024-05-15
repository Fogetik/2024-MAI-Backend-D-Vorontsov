
from django.urls import path
from . import views

urlpatterns = [
    path('',  views.allNews),
    path('profile',  views.profile),
    path('search',  views.findNews),
    path('new',  views.newNews)
]