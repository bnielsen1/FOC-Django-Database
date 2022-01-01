from django import forms
from django.db import models
from django import forms
from django.db.models import fields

from .models import PO, OrderedPart, Shippment, Part

class POShippmentForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.selected_po = kwargs.pop('selected_po')
        self.po_parts = self.selected_po.orderedpart_set.all()
        super().__init__(*args, **kwargs)
        for part in self.po_parts:
            self.fields['part_choice_%s' % part.part_number] = forms.BooleanField()

    #date_shipped = forms.DateTimeField()
    #date_received = forms.DateTimeField()
    shipped_from = forms.CharField(max_length=16)
    shipped_to = forms.CharField(max_length=16)
    shipper_receiver_id = forms.CharField(max_length=16)
    description = forms.CharField(max_length=128)
    manager = forms.CharField(max_length=64)
    notes = forms.CharField(max_length=256)
    #due_date = forms.DateTimeField()