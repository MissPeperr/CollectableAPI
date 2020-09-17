"""Module for Collectable"""
from django.db import models
from collectableapp.models import Collection

class Collectable(models.Model):
    """ Model class for Collectable"""
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    bought_price = models.FloatField()
    sold_price = models.FloatField(null=True)
    imageURL = models.URLField()
    is_sold = models.BooleanField(default=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="collection")

    class Meta:
        verbose_name = ("collectable")
        verbose_name_plural = ("collectables")

    def __str__(self):
        return self.title
