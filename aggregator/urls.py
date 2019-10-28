from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.terminal_home, name='index'),
    path('latest/',views.terminal_news,name='terminal_news'),
    path('sign-in/',views.sign_in,name='sign-in')
]