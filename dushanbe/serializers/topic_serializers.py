# from dushanbe.models import Topic
# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
#
#
# # Topic Create Serializer
# class TopicCreateSerializer(serializers.ModelSerializer):
#     topic_name = serializers.CharField(max_length=250, validators=[UniqueValidator(queryset=Topic.objects.all())])
#
#     class Meta:
#         model = Topic
#         fields = ('id', 'topic_name', 'active_status')
#
#
# # Topic Update Serializer
# class TopicUpdateSerializer(serializers.ModelSerializer):
#     topic_name = serializers.CharField(required=False, max_length=250, validators=[UniqueValidator(queryset=Topic.objects.all())])
#
#     class Meta:
#         model = Topic
#         fields = ('id', 'topic_name', 'active_status')
#
#
# # Topic List Serializer
# class TopicListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Topic
#         fields = ('id', 'topic_name', 'active_status')
#
#
