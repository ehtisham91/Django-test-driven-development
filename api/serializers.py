from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    # serializer to map the model instance into Json Format
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')