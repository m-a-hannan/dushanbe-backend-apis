# import pytz
# import inspect
# from datetime import datetime
# from django.dispatch import receiver
# from django.db.models.signals import post_save, pre_save
# from hrm_project.models import File, Project, Issue, SubIssue
# from hrm_project.helpers.random_string import random_string_id
# from hrm_project.helpers.convert_localtime import convert_to_localtime
#
#
# # Project
# # datetime converted to local datetime using branch timezone
# @receiver(pre_save, sender=Project)
# def project_created_datetime_conversion_to_local(sender, instance, **kwargs):
#     timezone = pytz.timezone(instance.branch.branch_timezone)
#     branch_timezone_now = datetime.now(timezone)
#     local_datetime = convert_to_localtime(branch_timezone_now)
#     instance.created_datetime = local_datetime
#
#
# # Project
# # assign "request.user" into "created_by" property & hard coded to get "request.user" for "pre_save" signal
# @receiver(pre_save, sender=Project)
# def assign_request_user_to_created_by(sender, instance, **kwargs):
#     for frame_record in inspect.stack():
#         if frame_record[3] == 'get_response':
#             request = frame_record[0].f_locals['request']
#             # assigned "request.user" into "created_by" property
#             instance.created_by = request.user
#             break
#     else:
#         request = None
#
#
# # Issue
# # assign self issue to parent_issue
# # @receiver(pre_save, sender=Issue)
# # def assign_self_issue_to_parent_issue(sender, instance, **kwargs):
# #     instance.parent_issue = instance
#
#
# # Issue
# # datetime converted to local datetime using branch timezone
# @receiver(pre_save, sender=Issue)
# def issue_created_datetime_conversion_to_local(sender, instance, **kwargs):
#     timezone = pytz.timezone(instance.project.branch.branch_timezone)
#     branch_timezone_now = datetime.now(timezone)
#     local_datetime = convert_to_localtime(branch_timezone_now)
#     instance.created_datetime = local_datetime
#
#
# # SubIssue
# # datetime converted to local datetime using branch timezone
# @receiver(pre_save, sender=SubIssue)
# def sub_issue_datetime_conversion_to_local(sender, instance, **kwargs):
#     timezone = pytz.timezone(instance.issue.project.branch.branch_timezone)
#     branch_timezone_now = datetime.now(timezone)
#     local_datetime = convert_to_localtime(branch_timezone_now)
#     instance.updated_at = local_datetime.date()
#     instance.running_datetime = local_datetime
#     instance.completed_datetime = local_datetime
#
#
# # SubIssue
# # assign "request.user" into "assignee" property & hard coded to get "request.user" for "pre_save" signal
# @receiver(pre_save, sender=SubIssue)
# def assign_request_user_to_assignee(sender, instance, **kwargs):
#     for frame_record in inspect.stack():
#         if frame_record[3] == 'get_response':
#             request = frame_record[0].f_locals['request']
#             instance.assignee = request.user
#             break
#     else:
#         request = None
#
#
# # Issue
# # "issue_id" generating
# @receiver(pre_save, sender=Issue)
# def generate_issue_id(sender, instance, **kwargs):
#     instance.issue_id = random_string_id(8)
#
#
# # SubIssue
# # "sub_issue_id" generating
# @receiver(pre_save, sender=SubIssue)
# def generate_sub_issue_id(sender, instance, **kwargs):
#     instance.sub_issue_id = random_string_id(8)