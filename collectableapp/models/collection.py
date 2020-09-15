"""Module for Collection"""
from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    """ Model class for Collection"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("collection")
        verbose_name_plural = ("collections")

    def __str__(self):
        return f'{self.title}: {self.description}'
