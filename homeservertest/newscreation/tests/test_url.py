
from rest_framework import status
from django.urls import path, reverse
from rest_framework.test import URLPatternsTestCase
from newscreation.views import get_news



class AccountTests(URLPatternsTestCase):
    urlpatterns = [
        path('', get_news, name='main'),
    ]

    def test_url_main(self):
        
        url = reverse('main')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

