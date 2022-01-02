from django.urls import path
from . import views
from django.contrib import admin

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('po/', views.po_list, name='po_list'),
    path('po/<int:po_id>/', views.po_view, name='po_view'),
    path('po/<int:po_id>/create_shippment', views.shippment_from_po, name='shippment_from_po'),
    path('po/shippments', views.shippment_list, name='shippment_list'),
    path('parts/', views.part_list, name='part_list'),
    path('parts/add', views.part_add, name='part_add'),
    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/add', views.vendor_add, name='vendor_add'),
]
