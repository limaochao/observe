from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from cameras.models import Cameras
from django.http import HttpResponse


@login_required(login_url="/login/")
def getCameras(request):
    user_id = request.user.id
    cameras = Cameras.objects.filter(user=user_id)
    for camera in cameras:
        print(camera.link)
    return render(
        request,
        "cameras/dashboard.html",
        {"cameras": cameras}
    )
