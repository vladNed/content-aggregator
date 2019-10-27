from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.meister_home, name='index')
]