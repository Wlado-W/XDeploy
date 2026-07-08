from django.shortcuts import render, get_object_or_404
from servers.models import Server
from .services import check_server

def server_check(request, pk):
    server = get_object_or_404(Server, id=pk)
    result = check_server(server)
    return render(request, "checker/result.html", {"result": result})