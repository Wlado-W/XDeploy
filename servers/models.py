from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True, null=True)
    ip = models.GenericIPAddressField()

    ssh_port = models.IntegerField(default=22)
    ssh_user = models.CharField(max_length=50)
    ssh_password = models.CharField(max_length=100)

    api_url = models.URLField(blank=True, null=True)
    api_login = models.CharField(max_length=50, blank=True, null=True)
    api_password = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.name} ({self.ip})"
