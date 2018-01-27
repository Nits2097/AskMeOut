from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def jargon(request):
    return render(request, 'jargon.html')

def forum(request):
    return render(request, 'forum.html')

def ask(request):
    return render(request, 'ask.html')

def logout_blog(request):
    print ("hi")
    if request.user.is_authenticated:
        logout(request)
        return render(request,'logout.html')
    else:
        return HttpResponseRedirect('/login/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        user = User.objects.create(
            first_name = name,
            username = username,
            )
        user.set_password(password)
        user.save()

        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('/ask/')
    else:
        return render(request,'register.html')   

def login_blog(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/ask/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'login.html')


# Create your views here.  