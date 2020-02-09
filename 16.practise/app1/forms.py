from django import forms
from .models import Details
from django.core.exceptions import ValidationError
 
class DetailForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    active = forms.BooleanField(required=False) # required=False makes the field optional
    created_on = forms.DateTimeField()
    last_logged_in = forms.DateTimeField()

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == "admin":
            raise ValidationError("Author name can't be 'admin/author'")
        return name_l

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def save(self):
        new_entry = Details.objects.create(
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            active = self.cleaned_data['active'],
            created_on = self.cleaned_data['created_on'],
            last_logged_in = self.cleaned_data['last_logged_in'],
            )
        return new_entry

class DetailForm2(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == "admin":
            raise ValidationError("Author name can't be 'admin/author'")
        return name_l

    def clean_email(self):
        return self.cleaned_data['email'].lower()



