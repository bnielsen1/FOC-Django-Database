from django.db.models import manager
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.http import JsonResponse
import datetime
from django.utils import timezone

from .models import PO, Part, Shippment, Vendor
from .forms import POShippmentForm, PartForm

def index(request):
    return render(request, 'polls/index.html')

def po_list(request):
    object_list = PO.objects.all()
    return render(request, 'polls/po_list.html', {'object_list': object_list})

def po_view(request, po_id):
    po = PO.objects.get(po_number=po_id)
    return render(request, 'polls/po_view.html', {'po': po})

def part_list(request):
    part_list = Part.objects.all()
    context= {
        'part_list': part_list,
    }
    return render(request, 'polls/part_list.html', context)

def part_add(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            p = Part(
                number = form.cleaned_data['number'],
                part_number = form.cleaned_data['part_number'],
                vendor = form.cleaned_data['vendor'],
            )
            return HttpResponseRedirect(reverse('polls:index'))

    form = PartForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/shippment_from_po.html', context)

def vendor_list(request):
    vendor_list = Vendor.objects.all()
    context= {
        'vendor_list': vendor_list,
    }
    return render(request, 'polls/vendor_list.html', context)

def shippment_from_po(request, po_id):
    this_po = PO.objects.get(po_number=po_id)
    if request.method == 'POST':
        form = POShippmentForm(request.POST, selected_po=this_po)
        if form.is_valid():
            s = Shippment(
                po=this_po,
                date_shipped = form.cleaned_data['date_shipped'],
                date_received = form.cleaned_data['date_received'],
                shipped_from = form.cleaned_data['shipped_from'],
                shipped_to = form.cleaned_data['shipped_to'],
                shipper_receiver_id = form.cleaned_data['shipper_receiver_id'],
                description = form.cleaned_data['description'],
                manager = form.cleaned_data['manager'],
                notes = form.cleaned_data['notes'],
                due_date = form.cleaned_data['due_date'],
                )
            s.save()

            for part in form.po_parts:
                print(form.cleaned_data['is_received_%s' % part.part_number])
                if form.cleaned_data['is_received_%s' % part.part_number] == True:
                    part.is_shipped = True
                    part.shippment = s
                    part.save()
                if form.cleaned_data['quantity_received_%s' % part.part_number] > 0:
                    temp = form.cleaned_data['quantity_received_%s' % part.part_number]
                    part.quantity_received = part.quantity_received + temp
                    part.shippment.add(s)
                    part.save()
            
            return HttpResponseRedirect(reverse('polls:index'))

    form = POShippmentForm(selected_po=this_po)
    context = {
        'po_id': po_id,
        'po': this_po,
        'form': form,
    }
    return render(request, 'polls/shippment_from_po.html', context)
