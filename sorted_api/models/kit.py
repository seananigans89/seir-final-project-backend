
from django.db import models
from django.contrib.auth import get_user_model

from sorted_api.models.item import Item


class Kit(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200, blank=True)
  gearList = models.ManyToManyField('Item', related_name='kits', blank=True)
  category =  models.CharField(max_length=100, )
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      related_name='kits'
  )

  def __str__(self):
    return f"This item has a name of {self.name}"



