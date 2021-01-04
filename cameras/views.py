from django.db.models import query
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from cameras.models import Cameras
from django.http import HttpResponse


@login_required(login_url="/login/")
def getCameras(request):
    user_id = request.user.id
    cameras = Cameras.objects.filter(user=user_id)
    # print(cameras.values())
    return render(
        request,
        "cameras/camera_list.html",
        {"cameras": cameras}
    )

@login_required(login_url="/login/")
def viewCamera(request, camera_id):
    _queryset = Cameras.objects.filter(camera_id=camera_id).values("link")
    link = _queryset[0]["link"]
    print(link)
    return render(
        request,
        "cameras/dashboard.html",
        {"link": link}
    )


@login_required(login_url="/login/")
def sign_out(request):
    logout(request)
    return render(
        request, 
        'login/login.html'
    )
