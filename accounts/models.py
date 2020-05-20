from django.db import models
#from .forms import User
from django.contrib.auth.models import User

category_choices= (
    ("Data Structure and Algorithms","Data Structure and Algorithms"),
    ("Programming Languages","Programming Languages"),
    ("Web Development","Web Development"),
)
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')
    category=models.CharField(max_length=30,choices=category_choices,default="")
    usersfav=models.ManyToManyField(User,blank=True)


    def __str__(self):
        return self.title 

"""
class IsFavourite(models.Model):
    file = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.file.title+' - '+self.user.username

"""