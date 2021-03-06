from __future__ import unicode_literals
# don't forget to import this
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    # the new line we're adding
    user = models.OneToOneField(User, blank=True, null=True)
