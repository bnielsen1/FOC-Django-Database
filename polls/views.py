from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from .models import PO, Part, Vendor

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
