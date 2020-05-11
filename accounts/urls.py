from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logoutpage/',views.logoutpage, name='logoutpage'),
    path('register/',views.register,name='register'),
    path('frontpage/',views.frontpage, name='frontpage'),
]
