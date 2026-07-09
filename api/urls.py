from django.urls import path
from . import views

urlpatterns = [
    path("test/<int:server_id>/", views.test_connection, name="api_test_connection,"),
]