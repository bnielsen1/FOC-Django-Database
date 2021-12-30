from django.db import models

# Part/Vendor are used for drop down list and not data
# Other models are physical stuff that constantly gets added

class PO(models.Model):
    po_number = models.CharField(max_length=16)
    vendor = models.CharField(max_length=16)
    date = models.DateTimeField('date ordered')
    notes = models.CharField(max_length=256)

    def __str__(self):
        return self.po_number

class Part(models.Model): 
    number = models.CharField(max_length=32)
    part_name = models.CharField(max_length=32)
    vendor = models.CharField(max_length=16)

    def __str__(self):
        return self.part_name

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=32)
    vendor_id = models.CharField(max_length=32)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.vendor_name

class Shippment(models.Model):
    po = models.ForeignKey(PO, on_delete=models.CASCADE)
    ordered_parts = models.ManyToManyField
    date_shipped = models.DateTimeField('date shipped')
    date_received = models.DateTimeField('date received')
    shipped_from = models.CharField(max_length=16)
    shipped_to = models.CharField(max_length=16)
    shipper_receiver_id = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    manager = models.CharField(max_length=64)
    notes = models.CharField(max_length=256)
    due_date = models.DateTimeField('due date')

class OrderedPart(models.Model):
    po = models.ForeignKey(PO, on_delete=models.CASCADE)
    shippment = models.ForeignKey(Shippment, on_delete=models.SET_NULL, auto_created=False, blank=True, null=True)
    is_shipped = models.BooleanField(default=False)
    part_number = models.CharField(max_length=32)
    part_name = models.CharField(max_length=32)
    quantity = models.CharField(max_length=32)

    def __str__(self):
        return self.part_name + ' - ' + self.part_number + ' - PO: ' + self.po.po_number