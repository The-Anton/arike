from django.shortcuts import render
from dataclasses import field
from django.shortcuts import render
from patients.forms import FacilityCreateForm

from patients.models import Patient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class GenericPatientCreateView(CreateView):
    form_class = FacilityCreateForm
    template_name = 'patient/patient_create.html'
    success_url = "/dashboard"
    
class GenericPatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient/patient_update.html'
    success_url = "/dashboard"

class GenericPatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'

class GenericPatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/patient_delete.html'
    success_url = "/dashboard"

