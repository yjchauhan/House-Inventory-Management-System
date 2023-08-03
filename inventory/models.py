from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=25)
    

    def __str__(self):
        return self.name


class Items(models.Model):
    item_name = models.CharField(max_length=255)
    stock_no= models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    
    

