from shareplum import Site
from shareplum import Office365
from shareplum.site import Version
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response
from dushanbe.serializers.sharepoint.share_point_serializers import SharePointSerializer


# http://127.0.0.1:8000/api/sharepoint/
class SharePointView(APIView):

    def post(self, request):
        # SharePoint config
        sharepointUsername = "Bangladesh.IT1@ludwigpfeiffer.com"
        sharepointPassword = "A%vhTlN90Z%M"
        sharepointSite = "https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka"
        website = "https://ludwpfeiffer.sharepoint.com"
        authcookie = Office365(website, username=sharepointUsername, password=sharepointPassword).GetCookies()
        site = Site(sharepointSite, version=Version.v2016, authcookie=authcookie)
        # sharepoint_dir = site.List('python_sync')
        sharepoint_dir = site.List('Dushanbe API Data (Testing)')

        # test data
        # data = {
        #     'bill': 'random_Bill',
        #     'type': 'random_type',
        #     'material': 'random_material',
        #     'submission_date': '2021-02-17',
        #     'work_progress': 10,
        # }

        # print('----', request.data['Item Serial No'])

        data = [
            {
                "Bill Name": request.data["bill"],
                "Type Name": request.data["type"],
                "Material Name": request.data["material"],
                "Submission Date": request.data["submission_date"],
                "Work Progress": request.data["work_progress"],
                # "CreatedBy": request.data['Work Done'],
                # "Active Status": request.data['Work Done']
            }
        ]

        print('--data--', data)

        # POST (UpdateListItems)
        obj = sharepoint_dir.UpdateListItems(data=data, kind='New')

        print('--obj--', obj)

        return Response({"data": data}, status=status.HTTP_200_OK)

    def get(self, request):
        sharepointUsername = "Bangladesh.IT1@ludwigpfeiffer.com"
        # print('----', sharepointUsername)

        sharepointPassword = "A%vhTlN90Z%M"
        # print('----', sharepointPassword)

        sharepointSite = "https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka"
        # print('----', sharepointSite)

        website = "https://ludwpfeiffer.sharepoint.com"
        # print('----', website)

        authcookie = Office365(website, username=sharepointUsername, password=sharepointPassword).GetCookies()
        # print('----', authcookie)

        site = Site(sharepointSite, version=Version.v2016, authcookie=authcookie)
        # print('----', site)

        set_list = site.List('python_sync')
        # print('----', set_list)

        share_data = set_list.GetListItems('All Items')  # this will retrieve all items from list
        print('----', share_data)

        for obj in share_data:
            for k, v in obj.items():
                print('{}: {}'.format(k, v))

            print('----')
        # response_serializer = SharePointSerializer(share_data, many=True)

        return Response({"data": "OK"}, status=status.HTTP_200_OK)
