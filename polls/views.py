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
from .forms import POShippmentForm, PartForm, VendorForm

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
            form.save()
            return HttpResponseRedirect(reverse('polls:part_list'))

    form = PartForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/part_add.html', context)

def vendor_list(request):
    vendor_list = Vendor.objects.all()
    context = {
        'vendor_list': vendor_list,
    }
    return render(request, 'polls/vendor_list.html', context)

def vendor_add(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:vendor_list'))

    form = VendorForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/vendor_add.html', context)

def shippment_list(request):
    shippment_list = Shippment.objects.all()
    context = {
        'shippment_list': shippment_list
    }
    return render(request, 'polls/shippment_list.html', context)

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

            for ordered_part in form.po_parts:
                print(form.cleaned_data['is_received_%s' % ordered_part.part.name])
                if form.cleaned_data['is_received_%s' % ordered_part.part.name] == True:
                    ordered_part.is_shipped = True
                    ordered_part.shippment = s
                    ordered_part.save()
                if form.cleaned_data['quantity_received_%s' % ordered_part.part.name] > 0:
                    temp = form.cleaned_data['quantity_received_%s' % ordered_part.part.name]
                    ordered_part.quantity_received = ordered_part.quantity_received + temp
                    ordered_part.shippment.add(s)
                    ordered_part.save()
            
            return HttpResponseRedirect(reverse('polls:index'))

    form = POShippmentForm(selected_po=this_po)
    context = {
        'po_id': po_id,
        'po': this_po,
        'form': form,
    }
    return render(request, 'polls/shippment_from_po.html', context)
