from django.db import models
from stop.models import Stop
# Create your models here.

# route app

class Route(models.Model):
    source=models.ForeignKey(Stop,on_delete=models.CASCADE,  related_name='route_stop')
    destination=models.ForeignKey(Stop,on_delete=models.CASCADE, related_name='route_dest')
    distance=models.CharField(max_length=50)


    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.source.name} to {self.destination.name} - {self.distance} km"