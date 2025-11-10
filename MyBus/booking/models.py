from django.db import models
from django.contrib.auth.models import User
from Bus.models import Seat
from schedule.models import Schedule   # ⬅️ Import your existing Schedule model

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Booking(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="bookings")
    booked_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=15, choices=PAYMENT_STATUS, default='pending')
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calculate_total(self):
        """Calculate total dynamically based on selected seats"""
        seat_count = self.seat_bookings.count()
        return seat_count * self.schedule.price

    @property
    def total_amount(self):
        """
        If payment is completed, return the frozen final amount.
        Otherwise calculate fresh based on current price × seats.
        """
        if self.payment_status == 'paid' and self.final_amount:
            return self.final_amount
        return self.calculate_total()

    def save(self, *args, **kwargs):
        # Freeze the amount only when status becomes PAID
        if self.payment_status == 'paid' and self.final_amount is None:
            self.final_amount = self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking #{self.id} | {self.user.username} | ₹{self.total_amount}"


class SeatBooking(models.Model):
    """
    Connects individual seats to a booking and schedule.
    Prevents same seat from being booked twice for the same schedule.
    """
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="seat_bookings")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="seat_bookings")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="seat_bookings")

    passenger_name = models.CharField(max_length=100)
    passenger_age = models.PositiveIntegerField(null=True, blank=True)
    passenger_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    class Meta:
        unique_together = ('schedule', 'seat')  # ❌ Duplicate seat booking prevented

    def __str__(self):
        return f"{self.passenger_name} - Seat {getattr(self.seat, 'seat_number', self.seat.id)} | {self.schedule.date} | {getattr(self.schedule.bus, 'reg_no', '')}"
