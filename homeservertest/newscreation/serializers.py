from rest_framework import serializers
from .models import NewsLink

class NewsLinkSerializer(serializers.ModelSerializer):
    cat = serializers.StringRelatedField()

    class Meta:
        model = NewsLink
        fields = '__all__'