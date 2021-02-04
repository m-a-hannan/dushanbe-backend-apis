from django.db import models
from django.contrib.auth.models import User


# Bill Table
class Bill(models.Model):
    bill_name = models.CharField(max_length=500, unique=True, blank=True, null=True)
    active_status = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Bills'

    def __str__(self):
        return self.bill_name


# Type Table
class Type(models.Model):
    type_name = models.CharField(max_length=250, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.type_name


# Material Table
class Material(models.Model):
    material_name = models.TextField(blank=True, null=True)
    serial_no = models.PositiveIntegerField(unique=True, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.material_name


# BillSubmission Table
class BillSubmission(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=True, null=True, related_name='billsubmission_bill')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True, related_name='billsubmission_type')
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, related_name='billsubmission_material')

    submission_date = models.DateField(auto_now_add=True, editable=True, blank=True, null=True)
    work_progress = models.PositiveIntegerField(default=0, blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='billsubmission_created_by')

    class Meta:
        verbose_name_plural = 'Bill Submissions'

    def __str__(self):
        return self.bill.bill_name

    @property
    def serial_no(self):
        if self.material.serial_no:
            return self.material.serial_no
        return 'empty'

    @property
    def unit(self):
        if self.material.unit:
            return self.material.unit
        return 'empty'

    @property
    def quantity(self):
        if self.material.quantity:
            return self.material.quantity
        return 'empty'
