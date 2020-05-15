from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage/',views.loginpage, name='loginpage'),
    path('logoutpage/',views.logoutpage, name='logoutpage'),
    path('register/',views.register,name='register'),
    path('frontpage/',views.frontpage, name='frontpage'),
    path('upload/',views.upload, name='upload'),  
    path('index/',views.index,name='index'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    