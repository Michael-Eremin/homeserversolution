from django.shortcuts import render
from newscreation.models import NewsLink
from newscreation.serializers import NewsLinkSerializer
from rest_framework import viewsets


class NewsLinkViewSet(viewsets.ModelViewSet):
    """View data sorted by descending date and category. The first 11 items from the database. Format 'json'."""
    queryset = NewsLink.objects.all().order_by('-date_published', 'cat')[:11]
    serializer_class = NewsLinkSerializer


def get_news(requests):
    """Template rendering 'index.html'."""
    return render(requests, 'newscreation/index.html')
