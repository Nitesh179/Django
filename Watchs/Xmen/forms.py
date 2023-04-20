from django import forms

class Stud_form(forms.Form):
    #  this field name available in HTML:
    
    name=forms.CharField(max_length=120)
    marks=forms.IntegerField()