from django import forms

from facility.models import Facility

class FacilityCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "p-1 my-2 w-full rounded-lg bg-white-100"
    class Meta:
        model = Facility
        fields = ["name","address", "pin_code", "phone_number", "kind"]


class FacilityUpdateForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["name","address", "pin_code", "phone_number", "kind"]