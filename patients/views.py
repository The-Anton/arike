from django.shortcuts import render
from dataclasses import field
from django.shortcuts import render
from patients.forms import DiseaseHistoryCreateForm, DiseaseHistoryUpdateForm, FamilyCreateForm, FamilyUpdateForm, PatientCreateForm, PatientUpdateForm, TreatmentCreateForm, TreatmentUpdateForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from patients.models import DiseaseHistory, Family, Patient, Treatment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class AuthorisedPatientManager(LoginRequiredMixin):
    def get_queryset(self):
        return Patient.objects.all()

class AuthorisedFamilyManager(LoginRequiredMixin):
    def get_queryset(self):
        print("value===" + self.request.GET['pk'])
        return Family.objects.filter(patient=self.request.GET['pk'])

class AuthorisedTreatmentManager(LoginRequiredMixin):
    def get_queryset(self):
        return Treatment.objects.all()

class AuthorisedDiseaseHistoryManager(LoginRequiredMixin):
    def get_queryset(self):
        return DiseaseHistory.objects.all()
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
    
class GenericPatientUpdateView(AuthorisedPatientManager, UpdateView):
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
class GenericFamilyListView(AuthorisedFamilyManager, ListView):
    model = Family
    context_object_name = 'families'
    qureyset = Family.objects.all()
    template_name = 'patient/family/family_create.html' 
class GenericFamilyCreateView(CreateView):
    form_class = FamilyCreateForm
    template_name = 'patient/family/family_create.html'
    success_url = "/dashboard"
    
class GenericFamilyUpdateView(AuthorisedFamilyManager, UpdateView):
    form_class = FamilyUpdateForm
    template_name = 'patient/family/family_update.html'
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
    
class GenericDiseaseHistoryUpdateView(AuthorisedDiseaseHistoryManager, UpdateView):
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
    
class GenericTreatmentUpdateView(AuthorisedTreatmentManager, UpdateView):
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