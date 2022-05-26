from rest_framework import serializers
from .models import NewsLink


class NewsLinkSerializer(serializers.ModelSerializer):
    """Serialization of data from the database by all fields. Output field 'cat' not by 'id' number, but by 'name'."""
    cat = serializers.StringRelatedField()
    class Meta:
        model = NewsLink
        fields = '__all__'