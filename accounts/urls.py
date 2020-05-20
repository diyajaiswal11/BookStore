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
    path('books/',views.book_list, name='book_list'),
    path('uploadbook/',views.upload_book,name='upload_book'), 
    path('dsabooks/',views.dsabooks,name='dsabooks'), 
    path('cpbooks/',views.cpbooks,name='cpbooks'), 
    path('webbooks/',views.webbooks,name='webbooks'), 
    path('search/',views.search,name='search'),
    path('addfav/',views.addfav,name='addfav'),
    path('deletefav/',views.deletefav,name='deletefav'),
    path('viewfav/',views.viewfav,name='viewfav'),
    #path('addfavorite/',views.addfavorite,name='addfavorite'),
    #path('index/',views.index,name='index'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    