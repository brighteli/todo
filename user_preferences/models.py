from django.db import models
from django.contrib.auth.models import User


class UserPreference(models.Model):
    back_ground = models.CharField(
        max_length=150,
        default="",
    )
    profile_photo = models.FileField(
        upload_to="./", default="no-profile.jpg", blank=True, null=True
    )
    created_by = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, blank=True, null=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
