from django.shortcuts import render

# Create your views here.
from .models import Stop
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView,UpdateView,DeleteView

# importing custom form


class AddStop(CreateView):
    model = Stop
    fields = '__all__'
    template_name = 'stop/add_stop.html'
    success_url = reverse_lazy("view_stops")

class ViewStop(ListView):
    model = Stop
    context_object_name = 'stops'
    template_name = 'stop/stops.html'


class EditStop(UpdateView):
    model = Stop
    fields = '__all__'
    template_name = 'stop/edit_stop.html'
    success_url = reverse_lazy('view_stops')


class RemoveStop(DeleteView):
    model = Stop
    template_name = 'stop/del_stop.html'
    success_url = reverse_lazy('view_stops')    



    
    
        








