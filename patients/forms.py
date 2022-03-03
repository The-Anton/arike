from django import forms

from patients.models import Patient

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name","address", "pin_code", "phone_number", "kind"]


class PatientFacilityForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name","address", "pin_code", "phone_number", "kind"]