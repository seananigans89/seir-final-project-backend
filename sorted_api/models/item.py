from django.db import models
from django.contrib.auth import get_user_model



class Item(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  serial_number = models.CharField(max_length=100)
  quantity = models.IntegerField(default=1)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return f"This item has a name of {self.name}"