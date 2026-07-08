from django.shortcuts import render
from servers.models import Server

def index(request):
    return render(request,"dashboard/index.html")

def index (request):
    context = {"server_count": Server.objects.count(),}
    return render(request, "dashboard/index.html", context)