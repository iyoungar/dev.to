from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import CreateUserForm
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return render (request, "signup.html", {})
    
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Acount was created for user: '+user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'signup.html', context)
        

def login(request):
    if request.user.is_authenticated:
        return render (request, "login.html", {})
    
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main.html')
            else:
                messages.info(request, "Username or Password is incorrect")
        context = {}
        return render(request, 'login.html', context)




    



