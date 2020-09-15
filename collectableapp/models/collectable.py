"""Module for Collectable"""
from django.db import models

class Collectable(models.Model):
    """ Model class for Collectable"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    boughtPrice = models.FloatField()
    soldPrice = models.FloatField()
    imageURL = models.URLField()

    class Meta:
        verbose_name = ("collectable")
        verbose_name_plural = ("collectables")

    def __str__(self):
        return self.title
