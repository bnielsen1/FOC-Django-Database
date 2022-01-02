from django.db import models

# Part/Vendor are used for drop down list and not data
# Other models are physical stuff that constantly gets added

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=32)
    vendor_id = models.CharField(max_length=32)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.vendor_name

class PO(models.Model):
    po_number = models.CharField(max_length=16)
    vendor = models.ForeignKey(Vendor, models.DO_NOTHING, null=True)
    date = models.DateField()
    notes = models.CharField(max_length=256)

    def __str__(self):
        return self.po_number

class Part(models.Model): 
    number = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Shippment(models.Model):
    po = models.ForeignKey(PO, on_delete=models.CASCADE)
    date_shipped = models.DateField()
    date_received = models.DateField()
    shipped_from = models.CharField(max_length=16)
    shipped_to = models.CharField(max_length=16)
    shipper_receiver_id = models.CharField(max_length=16)
    description = models.CharField(max_length=128, null=True)
    manager = models.CharField(max_length=64)
    notes = models.CharField(max_length=256, null=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return 'ID: ' + self.shipper_receiver_id + ' || DATE: ' + str(self.date_received) + ' || PO: ' + self.po.po_number

class OrderedPart(models.Model):
    initialized = False
    po = models.ForeignKey(PO, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING, null=True)
    part = models.ForeignKey(Part, on_delete=models.DO_NOTHING, null=True)
    shippment = models.ManyToManyField(
        Shippment, 
        auto_created=False, 
        blank=True, 
        null=True
        )
    is_shipped = models.BooleanField(default=False)
    quantity_received = models.IntegerField(default=0)
    quantity_expected = models.IntegerField()

    def __str__(self):
        return self.part.name + ' || ' + self.part.number + ' || PO: ' + self.po.po_number