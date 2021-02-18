from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from dushanbe.serializers.sharepoint.share_point_serializers import SharePointSerializer


# Accessing Data from SharePoint DB
class SharePointView(APIView):

    # POST (Testing): http://127.0.0.1:8000/api/sharepoint/
    def post(self, request):
        sharepoint_username = "Bangladesh.IT1@ludwigpfeiffer.com"
        sharepoint_password = "A%vhTlN90Z%M"
        sharepoint_url = "https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka"
        sharepoint_website = "https://ludwpfeiffer.sharepoint.com"
        sharepoint_authcookie = Office365(sharepoint_website, username=sharepoint_username,
                                          password=sharepoint_password).GetCookies()
        site = Site(sharepoint_url, version=Version.v2016, authcookie=sharepoint_authcookie)
        # sharepoint_list_directory = site.List('python_sync') # Jahid
        sharepoint_list_directory = site.List('dushanbe_api_testing')  # Siyam

        # Siyam
        data = [
            {
                "serial no": request.data["serial no"],
                "bill": request.data["bill"],
                "type": request.data["type"],
                "material": request.data["material"],
                "unit": request.data["unit"],
                "quantity": request.data["quantity"],
                "created_by": request.data['created_by'],
                "work_progress": request.data["work_progress"],
                "active_status": request.data['active_status'],
                "submission_date": request.data["submission_date"]

            }
        ]

        # Jahid
        # data = [
        #     {
        #         "Item Serial No": request.data["Item Serial No"],
        #         "Name of work including materials": request.data["Name of work including materials"],
        #         "Units": request.data["Units"],
        #         "Quantity": request.data["Quantity"],
        #         "Date": request.data["Date"],
        #         "Work Done": request.data["Work Done"]
        #     }
        # ]

        obj = sharepoint_list_directory.UpdateListItems(data=data, kind='New')

        print('--obj--', obj)

        return Response({"data": data}, status=status.HTTP_200_OK)

    # GET : http://127.0.0.1:8000/api/sharepoint/
    def get(self, request):
        sharepoint_username = "Bangladesh.IT1@ludwigpfeiffer.com"
        sharepoint_password = "A%vhTlN90Z%M"
        sharepoint_url = "https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka"
        sharepoint_website = "https://ludwpfeiffer.sharepoint.com"
        sharepoint_authcookie = Office365(sharepoint_website, username=sharepoint_username,
                                          password=sharepoint_password).GetCookies()
        site = Site(sharepoint_url, version=Version.v2016, authcookie=sharepoint_authcookie)
        sharepoint_list_directory = site.List('python_sync')  # Jahid
        # sharepoint_list_directory = site.List('Dushanbe API Data (Testing)') # Siyam
        sharepoint_data = sharepoint_list_directory.GetListItems('All Items')

        data = []

        for item in sharepoint_data:
            data.append(item)

        return Response({"data": data}, status=status.HTTP_200_OK)
