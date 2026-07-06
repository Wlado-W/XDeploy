from django.contrib import admin
from .models import Server

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ("name", "ip", "country", "is_active", "created_at")
    search_fields = ("name", "ip", "country")
    list_filter = ("is_active", "created_at")
