from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)
    age = models.IntegerField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='wines/', null=True, blank=True)

    def __str__(self):
        return self.name
