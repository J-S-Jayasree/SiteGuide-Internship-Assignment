from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from vehicles.models import Vehicle
# Create your views here.
class VehicleList(ListView):
    model = Vehicle

class VehicleView(DetailView):
    model = Vehicle

class VehicleCreate(CreateView):
    model = Vehicle
    fields = ['name', 'description']
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = ['name', 'description']
    success_url = reverse_lazy('vehicle_list')

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
