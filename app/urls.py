from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bsw/', views.bsw, name='bsw'),
    path('resources/', views.resources, name='resources'),
    path('intro/', views.intros, name='intros'),
    path('intro/hostel/<str:title>/', views.hostel_intros, name='hostel_intros'),
    path('intro/year/<str:title>/', views.year_intros, name='year_intros'),
    path('intro/create/', views.create_intro, name='create_intro'),
    path('intro/<str:username>/', views.intro, name='intro'),
    path('signin/', views.signin, name='signin'),
    path('register/<str:token>/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('reset/<str:token>/', views.reset, name='reset'),
]