from dataclasses import field
from django.shortcuts import render
from facility.forms import FacilityCreateForm, FacilityUpdateForm
from django.views.generic.list import ListView

from facility.models import Facility
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorisedFaclityManager(LoginRequiredMixin):
    def get_queryset(self):
        return Facility.objects.all()
class GenericFacilityListView(ListView):
    model = Facility
    context_object_name = 'facilities'
    qureyset = Facility.objects.all()
    template_name = 'facility/facility_list.html' 
class GenericFacilityCreateView(CreateView):
    form_class = FacilityCreateForm
    template_name = 'facility/facility_create.html'
    success_url = "/dashboard"
    
class GenericFacilityUpdateView(AuthorisedFaclityManager, UpdateView):
    form_class = FacilityUpdateForm
    template_name = 'facility/facility_update.html'
    success_url = "/dashboard"

class GenericFacilityDetailView(DetailView):
    model = Facility
    template_name = 'facility/facility_detail.html'

class GenericFacilityDeleteView(DeleteView):
    model = Facility
    template_name = 'facility/facility_delete.html'
    success_url = "/dashboard"
