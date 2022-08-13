from django.db import models
from varietal.models import varietal
from winery.models import Winery

class Wine(models.Model):
    name = models.CharField(max_length=50)
    winery = models.ForeignKey(Winery, on_delete=models.CASCADE)
    varietal = models.ForeignKey(varietal, on_delete=models.CASCADE)
    age = models.IntegerField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='wines/', null=True, blank=True)

    def __str__(self):
        return self.name
