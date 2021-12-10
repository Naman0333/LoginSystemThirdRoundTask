from django.shortcuts import render,redirect
from . forms import *
from django.views import generic
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'loginForm/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}!!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context ={
        'form' : form,
    }
    return render(request,'loginForm/register.html',context)
