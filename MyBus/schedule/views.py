from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Schedule
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView,UpdateView,DeleteView

# importing custom form


class AddSchedule(CreateView):
    model = Schedule
    fields = '__all__'
    template_name = 'schedule/add_schedule.html'
    success_url = reverse_lazy("view_schedules")

class ViewSchedule(ListView):
    model = Schedule
    context_object_name = 'schedules'
    template_name = 'schedule/schedules.html'


class EditSchedule(UpdateView):
    model = Schedule
    fields = '__all__'
    template_name = 'schedule/edit_schedule.html'
    success_url = reverse_lazy('view_schedules')


class RemoveSchedule(DeleteView):
    model = Schedule
    template_name = 'Schedule/del_schedule.html'
    success_url = reverse_lazy('view_schedules')    


# ----- schedules search Home page
from django.shortcuts import render
from django.http import JsonResponse
from .models import Schedule

def ajax_search_schedules(request):
    source = request.GET.get('source', "").strip()
    destination = request.GET.get('destination', "").strip()
    travel_date = request.GET.get('travel_date')

    schedules = Schedule.objects.select_related(
        "route", "bus", "route__source", "route__destination"
    )

    # Filter by Source City
    if source:
        schedules = schedules.filter(route__source__city__iexact=source)

    # Filter by Destination City
    if destination:
        schedules = schedules.filter(route__destination__city__iexact=destination)

    # Filter by Travel Date
    if travel_date:
        schedules = schedules.filter(date=travel_date)

    html = render(request, 'schedule/includes/schedules_results.html', {
        'schedules': schedules
    }).content.decode('utf-8')

    return JsonResponse({'html': html})
