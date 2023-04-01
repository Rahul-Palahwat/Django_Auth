from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


# to import django auth for users
from django.contrib.auth.models import User

# for logout
from django.contrib.auth import logout, authenticate, login


def index(request):
    # return HttpResponse("This is home page")
    print(request.user, "Hello user")
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def Userlogin(request):
    # return HttpResponse("This is login page")
    if request.method == "POST":
        # check if user has entered correct caredentials
        print("Hello world")
        name = request.POST.get('name')
        password = request.POST.get('password')

        print(name, password)
        user = authenticate(username=name, password=password)
        if user is not None:
            # return render(request, 'index.html')
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def Userlogout(request):
    # return HttpResponse("This is logout page")
    logout(request)
    return redirect('/login')
