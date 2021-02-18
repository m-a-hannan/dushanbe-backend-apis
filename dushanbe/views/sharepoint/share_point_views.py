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
        return Response({"data": "posted"}, status=status.HTTP_201_CREATED)

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
        # print('----', share_data)

        data = {}
        list_data = []

        for item in share_data:
            print('----', item)
            for k, v in item.items():
                print('{}: {}'.format(k, v))

        # response_serializer = SharePointSerializer(share_data, many=True)

        return Response({"data": "OK"}, status=status.HTTP_200_OK)
