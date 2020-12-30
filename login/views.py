from django.shortcuts import render,redirect
from . import models
from logger import logger
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            try:
                user = authenticate(username=username, password=password)
                print(user)
                if user:
                    login(request, user)
                    return redirect( "/cameras/" )
                else:
                    message = "密码错误"

            except Exception as e:
                message = "用户不存在"
            
            return render(
                request, 
                'login/login.html',
                { 'error_msg': message }
            )
        return render(request, 'login/login.html')
    elif request.method == 'GET':
        return render(
            request, 
            'login/login.html'
        )

def register(request):
    pass
    return render(request, 'login/register.html')

def sign_out(request):
    logout(request)
    return render(
        request, 
        'login/login.html'
    )
