from django.forms import ModelForm
from .models import Book, User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class BookForm(ModelForm):

    title = forms.CharField(
        label= "Book Title" ,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Book Title'
            }
        )
    )

    description = forms.CharField(
        label= "Book Description" ,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Book Description'
            }
        )
    )

    body = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Write the Story here !'
            }
        )
    )

    class Meta :
        model = Book
        fields = '__all__'

        exclude = ['author',]
        

class CustomUserCreation(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your Username'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your Email'
            }
        )
    )

    password1 = forms.CharField(
        label = "Password" , 
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter your Password',
            }
        )
    )

    password2 = forms.CharField(
        label = "Confirm Password" , 
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Confirm your Password'
            }
        )
    )

    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {field : None for field in fields}

