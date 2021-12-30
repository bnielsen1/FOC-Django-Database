from django import forms

from .models import PO, OrderedPart, Shippment

class POForm(forms.Form):
    po_number = forms.CharField(max_length=16)

#Look into ajax for js implentation (needed for changing choice prompts)