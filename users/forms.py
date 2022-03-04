from django import forms
from django.contrib.auth.models import User

from users.models import ArikeUser
from django.contrib.auth.forms import UserCreationForm  

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label='Email')  
    password1 = None  
    password2 = None  
    first_name = forms.CharField(label='First Name', min_length=2, max_length=150) 
    last_name = forms.CharField(label='Last Name', min_length=2, max_length=150) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["first_name"].widget.attrs["class"] = "p-1 my-2 w-full rounded-lg bg-white-100"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2
        
    class Meta:
        model = ArikeUser
        fields = ["first_name", "last_name", "email",]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = ArikeUser
        fields = ["first_name", "last_name", "email",]
