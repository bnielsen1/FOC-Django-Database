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
from .forms import POShippmentForm

def index(request):
    return render(request, 'polls/index.html')

def po_list(request):
    object_list = PO.objects.all()
    return render(request, 'polls/po_list.html', {'object_list': object_list})

def po_view(request, po_id):
    po = PO.objects.get(po_number=po_id)
    return render(request, 'polls/po_view.html', {'po': po})

def part_list(request):
    title = 'Parts (Newest to oldest)'
    data = serializers.serialize("python", Part.objects.all())
    print(data)
    context= {
        'data': data,
        'title': title,
    }
    return render(request, 'polls/generic_list.html', context)

def vendor_list(request):
    title = 'Vendors (Newest to oldest)'
    data = serializers.serialize("python", Vendor.objects.all())
    context= {
        'data': data,
        'title': title,
    }
    return render(request, 'polls/generic_list.html', context)

def shippment_from_po(request, po_id):
    this_po = PO.objects.get(po_number=po_id)
    if request.method == 'POST':
        form = POShippmentForm(request.POST, selected_po=this_po)
        if form.is_valid():
            s = Shippment(
                po=this_po,
                date_shipped = timezone.now(),
                date_received = timezone.now(),
                shipped_from = form.cleaned_data['shipped_from'],
                shipped_to = form.cleaned_data['shipped_to'],
                shipper_receiver_id = form.cleaned_data['shipper_receiver_id'],
                description = form.cleaned_data['description'],
                manager = form.cleaned_data['manager'],
                notes = form.cleaned_data['notes'],
                due_date = timezone.now(),
                )
            s.save()

            for part in form.po_parts:
                print(form.cleaned_data['part_choice_%s' % part.part_number])
                if form.cleaned_data['part_choice_%s' % part.part_number] == True:
                    part.is_shipped = True
                    part.shippment = s
                    part.save()
            
            return HttpResponseRedirect(reverse('polls:index'))

    form = POShippmentForm(selected_po=this_po)
    context = {
        'po': this_po,
        'form': form,
    }
    return render(request, 'polls/shippment_from_po.html', context)
