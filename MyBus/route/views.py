from django.shortcuts import render

# Create your views here.
from .models import Route
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView,UpdateView, DeleteView

# Creating records - 
class AddRoute(CreateView):
    model = Route 
    fields = '__all__' 
    success_url = reverse_lazy('view_routes')
    template_name = 'route/add_route.html'


class ViewRoute(ListView):
    model = Route
    context_object_name = 'routes'
    template_name = 'route/routes.html'

class EditRoute(UpdateView):
    model = Route
    template_name = 'route/edit_route.html'
    fields = '__all__'
    success_url = reverse_lazy('view_routes')

# Delete
class RemoveRoute(DeleteView):
    model = Route
    template_name = 'route/del_route.html'
    success_url = reverse_lazy('view_routes')

