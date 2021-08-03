from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
import re

class ShowManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be 2 characters or more"
        if len(postData['network']) < 2:
            errors['network'] = "Network must be 2 characters or more"
        if len(postData['description']) < 10:
            errors['network'] = "Description needs to be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date= models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()