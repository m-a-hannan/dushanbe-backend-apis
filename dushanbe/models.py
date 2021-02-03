from django.db import models
from django.contrib.auth.models import User


# Bill Table
class Bill(models.Model):
    bill_name = models.CharField(max_length=500, unique=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='bill_created_by')
    created_datetime = models.DateTimeField(auto_now_add=True, editable=True, blank=True, null=True)
    active_status = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Bills'

    def __str__(self):
        return self.bill_name


# Material Table
class Material(models.Model):
    material_name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.material_name


# NameOfWork Table
class NameOfWork(models.Model):
    work_name = models.CharField(max_length=250, blank=True, null=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=True, null=True, related_name='nameofwork_bill')
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, related_name='nameofwork_material')
    item_serial_no = models.CharField(max_length=20, unique=True, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    submission_date = models.DateField(auto_now_add=True, editable=True, blank=True, null=True)
    work_progress = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Name Of Work'

    def __str__(self):
        return self.work_name




