from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name='home'),
    path('profile/<str:username>', views.UserProfile, name='profile'),
    path('create/', views.Create, name='create'),
    path('body/<int:book_id>', views.BookBody, name='body'),
    path('read/<int:book_id>', views.ReadBook, name='read'),
    path('delete/<int:book_id>', views.DeleteBook, name='delete'),
    path('genre/<str:genre_name>', views.GenreSpecific, name='genre'),


    
    path('signUp/', views.SignUp, name='signUp'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]




