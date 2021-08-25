from django.contrib.auth import authenticate
from django.http import request
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout , login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        context = {'form': form,"title":"Register"}
        return render(request,'registration/register.html',context)
    


def register_data(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username,password=password)
                # print((user))
                # print((user.id))
                print(login(request,user))
                return redirect('/')
            else:
                context = {'form': form}
                return render(request,'registration/register.html',context)
        else:
            return redirect('/register')


def logout_view(request):
    logout(request)
    return redirect("/accounts/login/")
