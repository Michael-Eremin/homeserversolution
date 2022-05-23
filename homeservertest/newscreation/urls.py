from .views import get_news
from .views import NewsLinkViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path

router = SimpleRouter()
router.register(r'news', NewsLinkViewSet)


urlpatterns = [
    path('n/', get_news),
]

urlpatterns += router.urls

