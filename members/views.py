from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            messages.success(request,('There was a problem logging in. Please check your credentials and try again.'))
            # Return an 'invalid login' error message.
            return redirect('login')

    else:
        return render(request, "authenticate/login.html", {})
    
def logout_user(request):
    logout(request)
    messages.success(request,('You have been succesfully logged out!'))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You have succesfully created a doctor account!'))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {
        'form':form,
    })