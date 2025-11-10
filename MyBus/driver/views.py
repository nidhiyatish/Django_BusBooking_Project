from django.shortcuts import render

# Create your views here.


# Create your views here.
from .models import DriverProfile
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView,UpdateView,DeleteView

# importing custom form


class AddDriver(CreateView):
    model = DriverProfile
    fields = '__all__'
    template_name = 'driver/add_driver.html'
    success_url = reverse_lazy("view_drivers")

class ViewDriver(ListView):
    model = DriverProfile
    context_object_name = 'drivers'
    template_name = 'driver/drivers.html'


class EditDriver(UpdateView):
    model = DriverProfile
    fields = '__all__'
    template_name = 'driver/edit_driver.html'
    success_url = reverse_lazy('view_drivers')


class RemoveDriver(DeleteView):
    model = DriverProfile
    template_name = 'driver/del_driver.html'
    success_url = reverse_lazy('view_drivers')    



    
    
        








