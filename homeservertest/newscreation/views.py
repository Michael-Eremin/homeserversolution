from django.shortcuts import render
from .models import NewsLink
from .serializers import NewsLinkSerializer
from rest_framework import viewsets
from .datasite import get_list_data


# Create your views here.


class NewsLinkViewSet(viewsets.ModelViewSet):

    queryset = NewsLink.objects.all().order_by('-date_published', 'cat')[:11]
    serializer_class = NewsLinkSerializer

def get_news(requests):
    return render(requests, 'newscreation/index.html')

