from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import KeyViewSet

router = DefaultRouter()

router.register('key', KeyViewSet, basename='key')

urlpatterns = [
    path('', include(router.urls)),
]
