from django.db import models

# Create your models here.
from Bus.models import Bus
from route.models import Route

class Schedule(models.Model):
    bus= models.ForeignKey(Bus,on_delete=models.CASCADE,related_name="schedules")
    arrival_time=models.TimeField()
    departure_time=models.TimeField()
    price=models.IntegerField()
    date=models.DateField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE,related_name="schedules")
    
    def __str__(self):
        return f"{self.bus.reg_no}  {self.route.source.name} → {self.route.destination.name}- {self.date} | Rs. {self.price}"
