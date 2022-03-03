from django import forms

from facility.models import Facility

class FacilityCreateForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["name","address", "pin_code", "phone_number", "kind"]


class UpdateFacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["name","address", "pin_code", "phone_number", "kind"]