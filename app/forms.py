from django import forms
from .models import Product

class BarcodeForm(forms.Form):
    serial_no = forms.CharField(
        label='Serial Number', 
        max_length=100,
        widget=forms.TextInput(attrs={'autofocus': 'autofocus'})
    )
    part_no = forms.CharField(
        label='Part Number', 
        max_length=100
    )

class PartForm(forms.ModelForm):
    class Meta:
        model = Product #change table name
        fields = ['category','model_no','part_no'] #This will be shown in add_part form, serial no is auto-generated
