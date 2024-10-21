# Create your models here.
from django.db import models

class ShipmentRoute(models.Model):
    code = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    shipment_mode = models.CharField(max_length=255)
    fulfillment_method = models.CharField(max_length=255)
    molecule_or_test_type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    dosage_form = models.CharField(max_length=255)
    manufacturing_site = models.CharField(max_length=255)
    irst_line_designation = models.CharField(max_length=255)
    weight_kg = models.CharField(max_length=255)
    freight_cost_usd = models.CharField(max_length=255)
    line_item_insurance_usd = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255)
    first_line_designation = models.CharField(max_length=255)
    unit_per_pack = models.DecimalField(max_digits=10, decimal_places=2)
    line_item_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    line_item_value = models.DecimalField(max_digits=10, decimal_places=2)
    pack_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    scheduled_delivery_date = models.DateField()
    delivered_to_client_date = models.DateField()

    def __str__(self):
        return f"{self.origin} to {self.shipment_mode}"
