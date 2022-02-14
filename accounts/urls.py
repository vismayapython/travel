from django.urls import path
from . import views

urlpatterns= [
    path('register',views.register,name='register'),
    path('login',views.login,name='Login'),
    path('logout',views.logout,name='Logout')
]