# booking/views.py
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Booking, SeatBooking
from schedule.models import Schedule
from Bus.models import Seat

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class PaidBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking/paid_bookings.html"
    context_object_name = "bookings"
    ordering = ['-booked_at']

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user,
            payment_status='paid'
        ).select_related('schedule', 'schedule__bus', 'user')


class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = "booking/booking_detail.html"
    context_object_name = "booking"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


@require_GET
def seat_selection(request, schedule_id):
    schedule = get_object_or_404(
        Schedule.objects.select_related('bus', 'route', 'route__source', 'route__destination'),
        id=schedule_id
    )
    seats = schedule.bus.seats.all().order_by('id')
    return render(request, 'booking/seat_selection.html', {
        'schedule': schedule,
        'seats': seats,
    })


@require_GET
def api_booked_seats(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    booked = SeatBooking.objects.filter(schedule=schedule).values_list('seat_id', flat=True)
    return JsonResponse({'booked_seat_ids': list(booked)})


@login_required
@require_POST
def api_create_booking(request, schedule_id):
    """
    Creates a booking with passengers and seats
    Request body:
    {
      "passengers": [
        {"seat_id": 1, "name": "Amit"},
        {"seat_id": 2, "name": "Riya"}
      ]
    }
    """
    try:
        payload = json.loads(request.body.decode('utf-8'))
        passenger_data = payload.get('passengers', [])
        if not passenger_data or not isinstance(passenger_data, list):
            return HttpResponseBadRequest('Passengers list required')
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')

    schedule = get_object_or_404(Schedule, id=schedule_id)

    # extract seat ids
    seat_ids = [p.get('seat_id') for p in passenger_data]

    # Validate seat IDs belong to bus
    valid_seat_ids = set(Seat.objects.filter(bus=schedule.bus).values_list('id', flat=True))
    if not set(seat_ids).issubset(valid_seat_ids):
        return HttpResponseBadRequest('Invalid seat ids for this bus')

    # Validate names
    for p in passenger_data:
        if not p.get('name') or len(p.get('name').strip()) < 2:
            return HttpResponseBadRequest('Passenger name required and must be 2+ characters')

    with transaction.atomic():
        # Check if any seat already booked
        conflict = SeatBooking.objects.select_for_update().filter(schedule=schedule, seat_id__in=seat_ids)
        if conflict.exists():
            return JsonResponse({
                'ok': False,
                'error': 'Some seats already booked',
                'conflicts': list(conflict.values_list('seat_id', flat=True))
            }, status=409)

        # Create booking
        booking = Booking.objects.create(
            user=request.user,
            schedule=schedule,
            payment_status='pending'
        )

        # Save seats + passenger names
        seat_booking_objects = [
            SeatBooking(
                booking=booking,
                schedule=schedule,
                seat_id=p['seat_id'],
                passenger_name=p['name'].strip(),
                passenger_age=p['age'],
                passenger_gender=p['gender']
            )
            for p in passenger_data
        ]
        SeatBooking.objects.bulk_create(seat_booking_objects)

        total = booking.calculate_total()

    return JsonResponse({
        'ok': True,
        'booking_id': booking.id,
        'total_amount': float(total),
    })


@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(
        Booking.objects.prefetch_related('seat_bookings__seat'),
        id=booking_id,
        user=request.user
    )
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})
