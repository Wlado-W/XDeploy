from django.urls import path
from . import views

urlpatterns = [
    path("server/<int:pk>/", views.server_check, name="server_check"),
]