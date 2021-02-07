# import inspect
# from django.dispatch import receiver
# from django.db.models.signals import post_save, pre_save
# from dushanbe.helpers.random_string import random_string_id
# from dushanbe.models import Bill, Material, Type, BillSubmission


# # BillSubmission Table
# # assign "request.user" into "created_by" property & hard coded to get "request.user" for "pre_save" signal
# @receiver(pre_save, sender=BillSubmission)
# def assign_request_user_to_created_by(sender, instance, **kwargs):
#     for frame_record in inspect.stack():
#         if frame_record[3] == 'get_response':
#             request = frame_record[0].f_locals['request']
#             instance.created_by = request.user
#             break
#     else:
#         request = None






