from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag

# Create your models here.
class Task(models.Model):
    created_by = models.ForeignKey(
        User,
        default=None, on_delete=models.CASCADE, 
        blank=True, null=True
    )
    
    duration = models.DurationField(
        blank=""
    )

    task = models.CharField(
        max_length=100
    )

    date_created = models.DateField(
        auto_now=True
    )

     modified_date = models.DateTimeField(
        auto_now=True
    )
    
    tags = models.ManyToManyField(
        Tag,
        default='',
        blank=True
    )