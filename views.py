from django.shortcuts import render, redirect
from .forms import userRegistration,profileRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect ('homePage')
        else:
            messages.info (request, 'Email address or Password is incorrect')
            
    
    return render (request,'loginpage.html')


    def logoutUser(request):
    logout(request)
    return redirect('loginPage')