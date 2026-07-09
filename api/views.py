from django.shortcuts import render, get_object_or_404
from servers.models import Server
from .client import XUIClient

def test_connection(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    client = XUIClient(server)
    result = {"success": False, "message":"", "status": None, "inbounds": None,}
    try:
        if client.login():
            result["success"] = True
            result["status"] = client.get_server_status()
            result["inbounds"] = client.get_inbounds()
        else:
            result["message"] = "Не удалось авторизоваться в 3X-UI"
    except Exception as e:
        result["message"] = str(e)
    return render(request, "api/test_connection.html", {"server": server, "result": result},)    