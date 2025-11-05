from django.db import models

# Create your models here.


class Bus(models.Model):
    reg_no = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    category = models.CharField(
    max_length=50,
    choices=[
        ('express', 'Express'),
        ('non-express', 'Non Express'),
    ],
    default='express')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50, choices=[
        ('ac', 'AC'),
        ('non-ac','Non AC'),
    ])
    
    def __str__(self):
        return f"{self.reg_no} ({self.type})"
    
    @property
    def no_of_seats(self):
        return self.seats.count()
    
    
    
class BusImage(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='bus/images/')
    category = models.CharField(
        max_length=100,
        choices=(
            ('bus', 'Bus Exterior'),
            ('interior', 'Interior View'),
            ('luggage', 'Luggage Capacity'),
            ('seat', 'Seats'),
            ('driver_cabin', 'Driver Cabin'),
            ('ac', 'AC / Ventilation'),
            ('engine', 'Engine'),
        )
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} Image of {self.bus.name.capitalize()} Bus."


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='seats')
    type = models.CharField(max_length=50, choices=(
        ('sleeper', 'Sleeper'),
        ('sitting', 'Sitting')
    ))

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Seat #{self.id} | {self.type} | Bus : {self.bus.name}"
