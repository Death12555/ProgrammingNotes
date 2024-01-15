from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Features

def index(request):
    features= Features.objects.all()
    return render(request, 'index.html', {'features': features})

def count(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
    return render(request, 'count.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already used')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already used')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})