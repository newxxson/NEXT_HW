from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from Accounts.models import Account
# Create your views here.
def home(request):
    return render(request, 'home.html')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUsernameField(forms.CharField):
    """
    A custom field for the username that disables all validation.
    """
    def __init__(self, **kwargs):
        kwargs['validators'] = []
        super().__init__(**kwargs)

class CustomPasswordField(forms.CharField):
    """
    A custom field for the password that disables all validation.
    """
    def __init__(self, **kwargs):
        kwargs['validators'] = []
        kwargs['widget'] = forms.PasswordInput
        super().__init__(**kwargs)

class CreateUserForm(UserCreationForm):
    username = CustomUsernameField(max_length=150, label='Username')
    password1 = CustomPasswordField(label='Password', help_text=None)
    password2 = CustomPasswordField(label='Confirm Password', help_text='Confirm Password')

    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2']
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'The two password fields must match.')

class Authenticate(AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
    
def signup(request):
    if request.user.is_authenticated:
        return redirect('Blog:home')
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('Blog:home')
    
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('Blog:home')
    if request.method == 'POST':
        form = Authenticate(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('Blog:home')
        else:
            form = Authenticate()
            return render(request, 'login.html', {'form':form, 'wrong':True})
    else:
        form = Authenticate()
    
    
    return render(request, 'login.html', {'form':form, 'wrong':False})

def logout(request):
    auth.logout(request)
    return redirect('Blog:home')



def unauth(request):
    if request.user.is_authenticated:
        return redirect('Blog:home')
    return render(request, 'unauth.html')