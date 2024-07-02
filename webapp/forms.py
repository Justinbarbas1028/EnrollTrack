from django import forms # type: ignore
from django.forms import ModelForm # type: ignore
from .models import Program, Course

class LoginForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    age = forms.IntegerField(label='Age')
    phone = forms.CharField(label='Contact Number', max_length=20)
    email = forms.EmailField(label='Email')
    program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label='Select Program')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label='Select Course')