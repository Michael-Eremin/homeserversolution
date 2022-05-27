from unicodedata import name
from newscreation.views import get_news
from newscreation.views import NewsLinkViewSet
from rest_framework.routers import SimpleRouter
from django.urls import URLPattern, path


# URLs to get data in 'json' format.
router = SimpleRouter()
router.register(r'news', NewsLinkViewSet)
urlpatterns = router.urls


# URLs to get templates 'html'.
# urlpatterns = [
#     path('___/', _____),
# ]
# urlpatterns += router.urls