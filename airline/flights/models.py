from django.db import models

class airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f'{self.code} ({self.city})'
    
# Create your models here.
class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='departures')
    destination=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='arrivals')
    duration=models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination} in {self.duration}'