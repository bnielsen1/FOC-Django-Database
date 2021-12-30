from django.contrib import admin
from .models import PO, Part, Shippment, OrderedPart, Vendor

class OrderedPartInline(admin.StackedInline):
    model = OrderedPart
    extra = 0

class POAdmin(admin.ModelAdmin):
    fieldsets = [
        ('PO #', {'fields': ['po_number']}),
        ('Other Information', {'fields': ['vendor', 'date', 'notes'], 'classes': ['collapse']}),
    ]
    inlines = [OrderedPartInline]

class ShippmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('PO', {'fields': ['po']}),
        ('Dates', {'fields': ['date_shipped', 'date_received', 'due_date']}),
        ('Shipper/Receiver', {'fields': ['shipped_to', 'shipped_from', 'shipper_receiver_id']}),
        ('Other Information', {'fields': ['description', 'manager', 'notes'], 'classes': ['collapse']}),
    ]
    inlines = [OrderedPartInline]

admin.site.register(PO, POAdmin)
admin.site.register(Part)
admin.site.register(Shippment, ShippmentAdmin)
admin.site.register(OrderedPart)
admin.site.register(Vendor)
