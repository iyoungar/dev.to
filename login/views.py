from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import CreateUserForm
# Create your views here.

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Acount was created for user: '+user)
            return redirect('loginPage')

    context = {'form':form}
    
    # if request.user.is_authenticated:
    #     return render (request, "signup.html", {})
    
    # else:
          
    #     if request.method == 'POST':
    #         form = CreateUserForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             user = form.cleaned_data.get('username')
    #             messages.success(request, 'Acount was created for user: '+user)
    #             

    #     context = {'form': form}
    return render(request, 'signup.html', context)
        

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            messages.info(request, "username or password is incorrect")
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
     
#     if request.user.is_authenticated:
#         return render (request, "login.html", {})
    
#     else:
#         form = CreateUserForm()
#             
#         context = {}
      




    



