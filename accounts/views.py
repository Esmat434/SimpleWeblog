from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from .decorators import (
    login_required,logout_required
)
from .forms import UserCreationForm
# Create your views here.

@logout_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,'signup.html',{'form':form})
    form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

@logout_required
def login_user(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request,username = username, password = password)
        if user:
            login(request,user)
            return redirect('home')
        return render(request,'login.html',{'error_message':'your username or password is incorrect.'})
    return render(request,'login.html')

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request,'logout.html')