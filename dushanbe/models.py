from django.db import models
from django.contrib.auth.models import User


# Bill Table
class Bill(models.Model):
    bill_name = models.CharField(max_length=500, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Bills'

    def __str__(self):
        return self.bill_name

    @property
    def short_bill_name(self):
        return self.bill_name[0:151]


# Type Table
class Type(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=True, null=True, related_name='type_bill')
    type_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.type_name

    @property
    def short_type_name(self):
        return self.type_name[0:51]


# Material Table
class Material(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True, related_name='material_type')
    material_name = models.TextField(blank=True, null=True)
    serial_no = models.PositiveIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.material_name

    @property
    def short_material_name(self):
        return self.material_name[0:151]

    # for admin list_display only
    @property
    def short_bill_name(self):
        try:
            return self.type.bill.short_bill_name
        except:
            return 'empty'


# WorkSubmission Table
class WorkSubmission(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=True, null=True, related_name='workubmission_bill')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='workubmission_type')
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, related_name='workubmission_material')
    submission_date = models.DateField(editable=True, blank=True, null=True)
    work_progress = models.PositiveIntegerField(default=0, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='workubmission_created_by')
    active_status = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Work Submissions'

    def __str__(self):
        return self.bill.short_bill_name

    @property
    def serial_no(self):
        try:
            return self.material.serial_no
        except:
            return 'empty'

    @property
    def unit(self):
        try:
            return self.material.unit
        except:
            return 'empty'

    @property
    def quantity(self):
        try:
            return self.material.quantity
        except:
            return 'empty'




