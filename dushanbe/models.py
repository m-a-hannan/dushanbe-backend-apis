from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


# Bill Table
class Bill(models.Model):
    bill_name = models.CharField(max_length=500, blank=True, null=True)
    topic_name = models.CharField(max_length=250, blank=True, null=True)
    material_name = models.TextField(blank=True, null=True)
    item_serial_no = models.CharField(max_length=20, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    submission_date = models.DateField(auto_now_add=True, editable=True, blank=True, null=True)
    work_progress = models.PositiveIntegerField(default=0, blank=True, null=True)
    active_status = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Bills'
        unique_together = ['bill_name', 'item_serial_no']

    def __str__(self):
        return self.bill_name


# # Topic Table
# class Topic(models.Model):
#     topic_name = models.CharField(max_length=250, unique=True, blank=True, null=True)
#     active_status = models.BooleanField(default=True, blank=True, null=True)
#
#     class Meta:
#         verbose_name_plural = 'Topics'
#
#     def __str__(self):
#         return self.topic_name
#
#
# # Material Table
# class Material(models.Model):
#     material_name = models.TextField(blank=True, null=True)
#     item_serial_no = models.CharField(max_length=20, unique=True, blank=True, null=True)
#     unit = models.CharField(max_length=10, blank=True, null=True)
#     quantity = models.DecimalField(max_digits=8, decimal_places=2)
#     active_status = models.BooleanField(default=True, blank=True, null=True)
#
#     class Meta:
#         verbose_name_plural = 'Materials'
#
#     def __str__(self):
#         return self.material_name

