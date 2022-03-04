from django.shortcuts import render
from dataclasses import field
from django.shortcuts import render
from patients.forms import DiseaseHistoryCreateForm, DiseaseHistoryUpdateForm, FamilyCreateForm, FamilyUpdateForm, PatientCreateForm, PatientUpdateForm, TreatmentCreateForm, TreatmentUpdateForm
from django.views.generic.list import ListView

from patients.models import DiseaseHistory, Family, Patient, Treatment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# Patient View
class GenericPatientListView(ListView):
    model = Patient
    context_object_name = 'patients'
    qureyset = Patient.objects.all()
    template_name = 'patient/patient_list.html' 
class GenericPatientCreateView(CreateView):
    form_class = PatientCreateForm
    template_name = 'patient/patient_create.html'
    success_url = "/dashboard"
    
class GenericPatientUpdateView(UpdateView):
    form_class = PatientUpdateForm
    template_name = 'patient/patient_update.html'
    success_url = "/dashboard"

class GenericPatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'

class GenericPatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/patient_delete.html'
    success_url = "/dashboard"

# Family View
class GenericFamilyCreateView(CreateView):
    form_class = FamilyCreateForm
    template_name = 'patient/family/family_create.html'
    success_url = "/dashboard"
    
class GenericFamilyUpdateView(UpdateView):
    form_class = FamilyUpdateForm
    template_name = 'patient/family/pfamily_update.html'
    success_url = "/dashboard"

class GenericFamilyDetailView(DetailView):
    model = Family
    template_name = 'patient/family/family_detail.html'

class GenericFamilyDeleteView(DeleteView):
    model = Family
    template_name = 'patient/family/family_delete.html'
    success_url = "/dashboard"
# Disease History View
class GenericDiseaseHistoryCreateView(CreateView):
    form_class = DiseaseHistoryCreateForm
    template_name = 'patient/disease_history/disease_history_create.html'
    success_url = "/dashboard"
    
class GenericDiseaseHistoryUpdateView(UpdateView):
    form_class = DiseaseHistoryUpdateForm
    template_name = 'patient/disease_history/disease_history_update.html'
    success_url = "/dashboard"

class GenericDiseaseHistoryDetailView(DetailView):
    model = DiseaseHistory
    template_name = 'patient/disease_history/disease_history_detail.html'

class GenericDiseaseHistoryDeleteView(DeleteView):
    model = DiseaseHistory
    template_name = 'patient/disease_history/disease_history_delete.html'
    success_url = "/dashboard"


# Treatment View
class GenericTreatmentCreateView(CreateView):
    form_class = TreatmentCreateForm
    template_name = 'patient/treatment/treatment_create.html'
    success_url = "/dashboard"
    
class GenericTreatmentUpdateView(UpdateView):
    form_class = TreatmentUpdateForm
    template_name = 'patient/treatment/treatment_update.html'
    success_url = "/dashboard"

class GenericTreatmentDetailView(DetailView):
    model = Treatment
    template_name = 'patient/treatment/treatment_detail.html'

class GenericTreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'patient/treatment/treatment_delete.html'
    success_url = "/dashboard"