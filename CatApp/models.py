from django.db import models

# Create your models here.
class CatShop(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    breed = models.CharField(max_length=120)
    description = models.TextField()

    def __str__ (self):
        return self.name