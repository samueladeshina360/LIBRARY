from django.shortcuts import render, redirect
from .models import Book, Genre, User
from .forms import BookForm, CustomUserCreation
from django.http import HttpResponse
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


@login_required(login_url='login')
def Home(request):
    genres = Genre.objects.all()
    

    context = {'genres':genres}
    return render(request, 'main/home.html', context)

@login_required(login_url='login')
def Create(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        print(request.FILES)
        
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.author = request.user
            new_book.save()
            form.save_m2m()
            
            return redirect('body',book_id=new_book.id)


    context = {'form':form}
    return render(request, 'main/create.html', context)

@login_required(login_url='login')
def BookBody(request,book_id):

    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)

    if request.user != book.author:
        return redirect('home')

    if request.method == "POST":
        data = request.POST.get('body')
        data = data.strip()
        book.body = data
        book.save()

        return redirect('home')

    context = {'form':form, 'book':book}
    return render(request, 'main/body.html', context)

@login_required(login_url='login')
def ReadBook(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.body == None or len(book.body) == 0:
        return HttpResponse(
            """
                    Content Currently Undergoing Production ... visit later 
            """
        )


    context = {'book':book}
    return render(request,'main/read.html', context)

@login_required(login_url='login')
def DeleteBook(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.user != book.author:
        return redirect('home')

    if request.method == "POST" and book:
        book.delete()
        
        return redirect('home')

    context = {'book':book}
    return render(request,'main/delete.html', context)

@login_required(login_url='login')
def UserProfile(request, username):

    user = User.objects.get(username=username)
    books = Book.objects.filter( author = user ).order_by('-date_added')

    context = {'books' : books, 'user':user}
    return render(request, 'main/profile.html', context)

def SignUp(request):
    form = CustomUserCreation()

    if request.method == "POST":
        form = CustomUserCreation(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)
            messages.success(request, f"{request.user}, write out your ideas and stories.")
            return redirect('home')
        
        else:
            pass

    context = {'form':form}
    return render(request, 'main/signUp.html', context)

def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,f"{username} doesn't exist.")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            messages.success(request, f"{request.user}, write out your ideas and stories.")
            return redirect('home')
        
        else:
            messages.error(request,"Username or password doesn't match.")

    context = {}
    return render(request, 'main/login.html',context)

def logoutUser(request):

    if request.user.is_authenticated:
        logout(request)

    else:
        return redirect('signUp')
    
    return redirect('login')

def GenreSpecific(request, genre_name):
    genre = Genre.objects.get(genre = genre_name)
    
    context = {'genre':genre}
    return render(request,'main/genre.html', context)