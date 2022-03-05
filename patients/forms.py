from django import forms

from patients.models import DiseaseHistory, Family, Patient, Treatment

# Patient Form

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["address","first_name", "last_name", "birth_date", "email", "phone_number", "emergency_phone_number", "gender"]


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["address","first_name", "last_name", "birth_date", "email", "phone_number", "emergency_phone_number", "gender"]

# Disease History Form
class DiseaseHistoryCreateForm(forms.ModelForm):
    class Meta:
        model = DiseaseHistory
        fields = ["name", "remark"]


class DiseaseHistoryUpdateForm(forms.ModelForm):
    class Meta:
        model = DiseaseHistory
        fields = ["name", "remark"]

# Treatment Form

class TreatmentCreateForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ["discription"]


class TreatmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ["discription"]

# Family Form

class FamilyCreateForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ["first_name","last_name", "email", "birth_date", "phone_number", "address", "gender", "relation", "education"]


class FamilyUpdateForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ["first_name","last_name", "email", "birth_date", "phone_number", "address", "gender", "relation", "education"]
