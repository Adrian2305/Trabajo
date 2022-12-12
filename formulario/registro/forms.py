from django import forms

class PersonForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    email = forms.EmailField()
    photo = forms.ImageField(upload_to="images",null=True)
    