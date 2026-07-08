from django.urls import path
from . import views

urlpatterns = [
    path("", views.server_list, name="server_list"),
    path("create/", views.server_create, name="server_create"),
    path("edit/<int:pk>/", views.server_edit, name="server_edit"),
    path("delete/<int:pk>", views.server_delete, name="server_delete")

]