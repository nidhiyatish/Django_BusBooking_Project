from django.shortcuts import render, redirect

# Create your views here.
from .models import Bus, BusImage, Seat
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, UpdateView,DeleteView

# importing custom form
from .forms import BusImageForm

class AddBus(CreateView):
    model = Bus
    fields = '__all__'
    template_name = 'bus/add_bus.html'
    success_url = reverse_lazy("view_buses")

class ViewBuses(ListView):
    model = Bus
    context_object_name = 'buses'
    template_name = 'bus/buses.html'


class BusDetail(DetailView):
    model = Bus
    context_object_name = 'bus'
    template_name = 'bus/bus_details.html'

    # overriding this method to include extra context key i.e. form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusImageForm() # initializing BusImageForm to create a form object
        return context
    
    # Creating a post method to handle post requests in this view. 
    def post(self, request, pk):

        # filtering the bus for which we are adding picture
        this_bus = Bus.objects.get(id = pk)

        # collecting the submitted file and form data from request object and creating form object
        form = BusImageForm(request.POST, request.FILES)
        if form.is_valid():
            # getting bus_image object from the form data without pushing to DB
            bus_image = form.save(commit=False)

            # Assigning the current bus as the bus for the submitted image.
            bus_image.bus = this_bus
            bus_image.save()
            return redirect("bus_details", pk=this_bus.pk)
        else:
            print("Invalid form")
            return redirect("bus_details", pk=this_bus.pk)



class EditBus(UpdateView):
    model = Bus
    fields = '__all__'
    template_name = 'bus/edit_bus.html'
    success_url = reverse_lazy('view_buses')

class RemoveBus(DeleteView):
    model = Bus
    template_name = 'bus/del_bus.html'
    success_url = reverse_lazy('view_buses')    



# -----------------
class UpdateBusImage(UpdateView):
    model = BusImage
    template_name = 'bus/update_bus_image.html'
    form_class = BusImageForm

    def get_success_url(self):
        bus_id = self.object.bus.id
        return reverse_lazy('bus_details', kwargs={'pk': bus_id})
    
class DelBusImage(DeleteView):
    model = BusImage
    template_name = 'bus/del_bus_image.html'

    def get_success_url(self):
        bus_id = self.object.bus.id
        return reverse_lazy('bus_details', kwargs={'pk': bus_id})