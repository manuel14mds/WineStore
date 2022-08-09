from django import forms

class form_varietal(forms.Form):
    name = forms.CharField(max_length=100)
    features = forms.CharField(max_length=300)
    type_grape = forms.CharField(max_length=50)
    location = forms.CharField(max_length=100)
    winery = forms.CharField(max_length=70)
    wine = forms.CharField(max_length=50)