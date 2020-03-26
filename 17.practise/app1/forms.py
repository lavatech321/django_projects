from django import forms
from .models import Details
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


 
class DetailForm(forms.ModelForm):
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


class DetailForm2(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'

        widgets = {
            'name': forms.TextInput( 
                attrs={ 'class':"form-control" , 'id':"inputname" , 'placeholder':"Name"}),  
            'email': forms.EmailInput(
                attrs={ 'class':"form-control" , 'id':"inputEmail4" , 'placeholder':"Email"}),
            'password': forms.PasswordInput(
                attrs={ 'class':"form-control" , 'id':"inputPassword4" , 'placeholder':"Password"}),
            'confirm_password': forms.PasswordInput(
                attrs={ 'class':"form-control" , 'id':"confirm_inputPassword4" , 'placeholder':"Confirm Password"}),
            'phone_number': forms.TextInput(
                attrs={ 'class':"form-control" , 'id':"phno" , 'placeholder':"Phone Number" , }),  
            'address1': forms.TextInput(
                attrs = {'class':"form-control" ,'id':"inputAddress" ,'placeholder':"1234 Main St"}),
           'address2' : forms.TextInput(
                attrs = {'class':"form-control" , 'id':"inputAddress2", 'placeholder':"Apartment, studio, or floor"}),
            'city' : forms.TextInput(
                attrs = {'class':"form-control" , 'id':"inputCity"}),
            'state' : forms.Select(
                attrs = {"id":"inputState",'class':"form-control"}),
            'zip1' : forms.TextInput(
                attrs = {'class':"form-control",  'id':"inputZip"}),
            'checkbox': forms.CheckboxInput(
                attrs = {'class':"form-check-input",'id':"gridCheck"}),
           }


    def clean_name(self):
        name = self.cleaned_data['name']
        name_l = name.lower()
        if name_l == "admin":
            raise ValidationError("Author name can't be 'admin/author'")
        return name_l

    def clean_email(self):
        return self.cleaned_data['email'].lower()


class DetailForm3(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
        widgets = {
            'name': forms.TextInput( 
                attrs={ 'class':"form-control" , 'id':"inputname" , 'placeholder':"Name" , }),  
            'email': forms.EmailInput(
                attrs={ 'class':"form-control" , 'id':"inputEmail4" , 'placeholder':"Email"}),
            'password': forms.PasswordInput(
                attrs={ 'class':"form-control" , 'id':"inputPassword4" , 'placeholder':"Password"}),
            'confirm_password': forms.PasswordInput(
                attrs={ 'class':"form-control" , 'id':"confirm_inputPassword4" , 'placeholder':"Confirm Password"}),
            'phone_number': forms.TextInput(
                attrs={ 'class':"form-control" , 'id':"phno" , 'placeholder':"Phone Number" , }),  
            'address1': forms.TextInput(
                attrs = {'class':"form-control" ,'id':"inputAddress" ,'placeholder':"1234 Main St"}),
           'address2' : forms.TextInput(
                attrs = {'class':"form-control" , 'id':"inputAddress2", 'placeholder':"Apartment, studio, or floor"}),
            'city' : forms.TextInput(
                attrs = {'class':"form-control" , 'id':"inputCity"}),
            'state' : forms.Select(
                attrs = {"id":"inputState",'class':"form-control"}),
            'zip1' : forms.TextInput(
                attrs = {'class':"form-control",  'id':"inputZip"}),
            'checkbox': forms.CheckboxInput(
                attrs = {'class':"form-check-input",'id':"gridCheck"}),
           }
        labels = {
            'name': ('Enter Your Name'),
            'email': ('Enter Your Email'),
            'password': ('Enter your Password'),
            'confirm_password': ('Confirm your Password'),
            'address1': ('Enter Address I'),
            'address2': ('Enter Address II'),
            'city': ('City'),
            'state': ('State'),
            'zip1': ('Zip'),
            'checkbox': ('Agree Terms and Conditions'),
        }
        help_texts = {
            'zip1': ('Zipcode should be 6 digits'),
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
            'email': {
                'required': ('Email Address cannot be Empty'),
            },
            'password': {
                'required': ('Password is needed'),
            }
        }

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean_phone_number(self):
        no = str(self.cleaned_data['phone_number'])
        if len(no) < 9 or len(no) > 15:
            raise ValidationError("Invalid Phone Number")
            #self.add_error('phone_number', 'Invalid Phone Number') 
        return self.cleaned_data['phone_number']

    def clean_zip1(self):
        no = str(self.cleaned_data['zip1'])
        if len(no) != 6:
            raise ValidationError("Zip Code should be 6 digit")
            #self.add_error('phone_number', 'Invalid Phone Number') 
        return self.cleaned_data['zip1']

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']
        if password != confirm_password :
            raise ValidationError("Password Does not Match")
        return self.cleaned_data['confirm_password']

   
            
