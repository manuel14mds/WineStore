from django.db import models

# Create your models here.
class Winery(models.Model):
    name = models.CharField(max_length=40)
    specialty = models.CharField(max_length=40)
    owner_name = models.CharField(max_length=40)
    creation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name