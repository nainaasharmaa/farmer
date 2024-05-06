from django.urls import path, include
from .import views

urlpatterns=[
    path('',views.home, name='home'),
    path('auth/',views.auth, name='auth'),
    path('login/',views.login, name='login'),

]