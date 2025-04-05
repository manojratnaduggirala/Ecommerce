from django.db import models

class Compliance(models.Model):
    vendor = models.ForeignKey('products.Vendor', on_delete=models.CASCADE)
    compliance_type = models.CharField(max_length=255)
    approval_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending')

    def __str__(self):
        return f"{self.vendor.name} - {self.compliance_type}"
