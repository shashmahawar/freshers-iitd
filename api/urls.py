from django.urls import path
from . import views

urlpatterns = [
    path('checkKerberos/', views.checkKerberos, name='checkKerberos'),
    path('login/', views.login, name='login'),
    path('manageLike/', views.manageLike, name='manageLike'),
    path('forgot/', views.forgot, name='forgot'),
]