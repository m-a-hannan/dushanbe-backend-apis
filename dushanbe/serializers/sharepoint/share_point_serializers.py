from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# SharePoint Serializer for GET
class SharePointSerializer(serializers.Serializer):
    # sharepointUsername = serializers.CharField()
    # sharepointPassword = serializers.CharField()
    # sharepointSite = serializers.CharField()
    # website = serializers.CharField()
    # authcookie = serializers.CharField()
    # site = serializers.CharField()
    # set_list = serializers.CharField()
    # share_data = serializers.CharField()

    class Meta:
        fields = (
            'sharepointUsername', 'sharepointPassword', 'sharepointSite', 'website', 'authcookie', 'site', 'set_list',
            'share_data'
        )

