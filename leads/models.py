from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    message = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
