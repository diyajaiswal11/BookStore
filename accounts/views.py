from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout, get_user_model
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')  



def register(request):
    user=request.user
    if user.is_authenticated:
        return redirect('home') 
    else:
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('loginpage')
        else:
            form=CreateUserForm()    
        context = {'form':form }    
        return render(request,'register.html',context)

def loginpage(request):
    user = request.user
    if user.is_authenticated:
        return redirect('frontpage') 
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            if next:
                return redirect(next)
            return redirect('frontpage')
        
        context = {
            'form': form,
        }
        return render(request, 'loginpage.html', context)

def logoutpage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='frontpage')
def frontpage(request):
    #books=Book.objects.all()
    
    return render(request,'frontpage.html')  



@login_required(login_url='books')
def book_list(request):
    books=Book.objects.all() 

    return render(request,'book_list.html',{'books':books})

@login_required(login_url='books')
def dsabooks(request):
    books=Book.objects.filter(category="Data Structure and Algorithms")
    
    return render(request,'dsa.html',{'books':books})

@login_required(login_url='cpbooks')
def cpbooks(request):
    books=Book.objects.filter(category="Programming Languages")
    
    return render(request,'cp.html',{'books':books})

@login_required(login_url='webbooks')
def webbooks(request):
    books=Book.objects.filter(category="Web Development")
    
    return render(request,'web.html',{'books':books})


@login_required(login_url='uploadbook')
def upload_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('book_list') 

    else:
        form=BookForm()
    return render(request,'upload_book.html',{'form':form})



@login_required(login_url='search')
def search(request):

    query=request.GET['query']
    if query=="":
        books=Book.objects.none()
    elif len(query)>50:
        books=Book.objects.none()
    else:
        books1=Book.objects.filter(title__icontains=query)
        books2=Book.objects.filter(author__icontains=query)
        books=books1.union(books2)

    
    return render(request,'search.html',{'books':books , 'query':query})
    #return HttpResponse("This is search")
    


@login_required(login_url='addfav')
def addfav(request):
    current_user=request.user
    if request.method=="POST":
        book_title = request.POST.get('book_title')
        fav_book=Book.objects.filter(title=book_title).get()
        fav_book.usersfav.add(current_user)
        context = {

        }
        return render(request,'book_list.html',context)


@login_required(login_url='deletefav')
def deletefav(request):
    current_user=request.user
    if request.method=="POST":
        book_title = request.POST.get('book_title')
        fav_book=Book.objects.filter(title=book_title).get()
        fav_book.usersfav.remove(current_user)
        books=Book.objects.filter(usersfav=current_user)
        context = {
            'books':books
        }
        return render(request,'favorite.html',context)        

@login_required(login_url='viewfav')
def viewfav(request):
    current_user=request.user
    books=Book.objects.filter(usersfav=current_user)
    return render(request,'favorite.html',{'books':books})


"""
@login_required(login_url='addfavourite')
def addfavourite(request,bookid):
    current_user=request.user
    current_file=get_object_or_404(Book,pk=bookid)
    p, created = IsFavourite.objects.get_or_create(
    file = current_file,
    user = current_user,
    )
    if created:
        p.save()
    else:
        p.delete()
    return JsonResponse(
        {"status":"success"}
    )
"""



"""
@login_required(login_url='upload')
def upload(request):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['document'] 
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)
        context['url']=fs.url(name)
    return render(request,'upload.html')
"""
