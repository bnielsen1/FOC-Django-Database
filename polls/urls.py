from django.urls import path
from . import views
from django.contrib import admin

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('po/', views.po_list, name='po_list'),
    path('po/<int:po_id>/', views.po_view, name='po_view'),
    path('parts/', views.part_list, name='part_list'),
    path('vendors/', views.vendor_list, name='vendor_list')
]
