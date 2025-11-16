from django.db import models

class TmsUsers(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=20)
    email_id = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
