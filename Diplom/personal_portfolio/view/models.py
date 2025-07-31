from django.db import models
from django.contrib.auth.models import User


class View(models.Model):
    title = models.CharField(max_length=100)

