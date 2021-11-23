from django import forms
from django.forms import ModelForm
from .models import Customer
class ContactForm(forms.Form):
    yourname=forms.CharField(max_length=100,label="Your Name")
    Email=forms.EmailField(max_length=100,required=False,label="Your Email Address")
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)

class CustomerForm(ModelForm):
    required_css_class='required'
    class Meta:
        model=Customer
        fields=['CFullName','CAddress','CMobile','CEmail','CUserName','CPassword','CGender','CImage']
        labels={
            'CFullName':'Full Name',
            'CAddress':'Address',
            'CMobile':'Mobile',
            'CEmail':'Email Address',
            'CUserName':'User Name',
            'CPassword':'Password',
            'CGender':'Gender',
            'CImage':'Personal Image'
        }

class LoginForm(ModelForm):
    class Meta:
        model=Customer
        fields=('CUserName','CPassword')
        labels={
            'CUserName':'User Name',
            'CPassword':'Password'
        }

