from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=15, blank=True, null=True)
    user_grade = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user_name


class Complaints(models.Model):
    folio = models.CharField(max_length=10, unique=True, blank=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=False,null=False)
    date_ocurrence = models.DateTimeField(blank=False)
    date_created = models.DateTimeField(blank=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    status = models.CharField(max_length=20, blank=False)


class Comment(models.Model):
    complaint_id = models.ForeignKey(Complaints, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=2000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)