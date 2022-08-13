from django.db import models

class varietal(models.Model):
    name = models.CharField(max_length=100)
    features = models.CharField(max_length=300)
    type_grape = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    # winery = models.CharField(max_length=70)
    # wine = models.CharField(max_length=50)
