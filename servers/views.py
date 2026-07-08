from django.shortcuts import render, redirect, get_object_or_404
from .models import Server
from .forms import ServerForm

def server_list(request):
    servers = Server.objects.all()
    return render(request, "servers/list.html", {"servers":servers})

def server_create(request):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("server_list")
    return render(request, "servers/form.html", {"form":form})

def server_edit(request, pk):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, isinstance=server)
    if form.is_valid():
        form.save()
        return redirect("server_list")
    return render(request, "server/form.html", {"form":form})

def server_delete(request, pk):
    server = get_object_or_404(Server, pk=pk)
    server_delete()
    return redirect("server_list")