from django import forms

class UsersForm(forms.Form):
    num1=forms.CharField(label="value1", required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    num2=forms.CharField(label="value1",  widget=forms.TextInput(attrs={'class': "form-control"}) )
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))