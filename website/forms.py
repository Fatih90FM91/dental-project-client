from django import forms
from .models import Register



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields =('first_name' ,'last_name' ,'gender' ,'email' , 'phone' ,'date_of_birth' ,'house_number' ,'city' ,'state' , 'zipcode' ,'street' ,'how_hear_about_us' ,'question' ,'are_you_member')

        widgets = {

            'first_name' : forms.TextInput(attrs = {'class' : 'form-control-register'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'gender' : forms.Select(choices=Register.GenderType, attrs={'class' : 'form-control-register'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'phone' : forms.TextInput(attrs = {'class' : 'form-control-register'}),
            'date_of_birth' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'house_number' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'state' : forms.TextInput(attrs = {'class' : 'form-control-register'}),
            'zipcode' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'street' : forms.TextInput(attrs={'class' : 'form-control-register'}),
            'how_hear_about_us' : forms.Select(choices=Register.FindingType, attrs={'class' : 'form-control-register'}),
            'question' : forms.Textarea(attrs={'class' : 'form-control-register', 'placeholder': 'Do you have any Question?'}),
            'are_you_member' : forms.Select(choices=Register.MemberType, attrs={'class' : 'form-control-register'}),

        }
