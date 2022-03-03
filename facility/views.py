from dataclasses import field
from django.shortcuts import render
from facility.forms import FacilityCreateForm

from facility.models import Facility
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class GenericFacilityCreateView(CreateView):
    form_class = FacilityCreateForm
    template_name = 'facility/facility_create.html'
    success_url = "/dashboard"
    
class GenericFacilityUpdateView(UpdateView):
    model = Facility
    template_name = 'facility/facility_update.html'
    success_url = "/dashboard"

class GenericFacilityDetailView(DetailView):
    model = Facility
    template_name = 'facility/facility_detail.html'

class GenericFacilityDeleteView(DeleteView):
    model = Facility
    template_name = 'facility/facility_delete.html'
    success_url = "/dashboard"
