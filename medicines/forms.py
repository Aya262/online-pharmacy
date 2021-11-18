from django import forms

class ContactForm(forms.Form):
    yourname=forms.CharField(max_length=100,label="Your Name")
    Email=forms.EmailField(max_length=100,required=False,label="Your Email Address")
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)

