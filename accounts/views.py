

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login ,logout
from .form import NewUSerForm
from django.contrib.auth import (
    logout as logout_user,
    login as login_user,
    authenticate,
)
from django.contrib import messages



def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:product_list')
    else:
        form = NewUSerForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
            user = form.get_user()
            login_user(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('shop:product_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })


def logout(request):
    logout_user(request)
    #return render(request,"logout.html")
    messages.info(request, 'You\'ve been successfully logged out!')
    return redirect('shop:product_list')