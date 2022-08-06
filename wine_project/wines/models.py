from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
