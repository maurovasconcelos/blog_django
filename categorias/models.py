from django.db import models

class Categoria(models.Model):
  name_cat = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name_cat
