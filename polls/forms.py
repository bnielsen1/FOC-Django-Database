from django import forms
from django.db import models
from django import forms
from django.db.models import fields

from .models import PO, OrderedPart, Shippment, Part
from .widget import DatePickerInput

class POShippmentForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.selected_po = kwargs.pop('selected_po')
        self.po_parts = self.selected_po.orderedpart_set.filter(is_shipped=False)
        super().__init__(*args, **kwargs)
        for part in self.po_parts:
            self.fields['quantity_received_%s' % part.part_number] = forms.IntegerField(initial=0)
            self.fields['is_received_%s' % part.part_number] = forms.BooleanField(required=False)

    date_shipped = forms.DateField(widget=DatePickerInput)
    date_received = forms.DateField(widget=DatePickerInput)
    shipped_from = forms.CharField(max_length=16)
    shipped_to = forms.CharField(max_length=16)
    shipper_receiver_id = forms.CharField(max_length=16)
    description = forms.CharField(max_length=128, required=False)
    manager = forms.CharField(max_length=64)
    notes = forms.CharField(max_length=256, required=False)
    due_date = forms.DateField(widget=DatePickerInput, required=False)