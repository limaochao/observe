from django.shortcuts import render
from .models import OpsArticle
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from dwebsocket.decorators import accept_websocket, require_websocket
import os
import re

@login_required(login_url = "/login/")
def weatherops(request):
    snippets = OpsArticle.objects.all()
    return render(
        request, 
        "cameras/dashboard.html", 
        {"snippets": snippets}
    )
