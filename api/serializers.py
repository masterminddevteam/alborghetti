from rest_framework import serializers
from rest_framework.reverse import reverse

from worker.models import SpiderContent

class SpiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpiderContent
        fields = ('id', 'name', 'updated_on', 'category', 'content', 'content_length')
