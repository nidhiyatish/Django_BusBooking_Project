# booking/urls.py
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('all/', views.PaidBookingsView.as_view(), name='bookings'),
    path("details/<int:pk>/", views.BookingDetailView.as_view(), name="booking_details"),
    path('schedule/<int:schedule_id>/seats/', views.seat_selection, name='seat_selection'),
    path('api/schedule/<int:schedule_id>/booked-seats/', views.api_booked_seats, name='api_booked_seats'),
    path('api/schedule/<int:schedule_id>/create-booking/', views.api_create_booking, name='api_create_booking'),
    path('<int:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
