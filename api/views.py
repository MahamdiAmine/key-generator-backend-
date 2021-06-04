from rest_framework import viewsets

from key.models import Key
from key.serializers import KeySerializer



class KeyViewSet(viewsets.ModelViewSet):
    serializer_class = KeySerializer
    queryset = Key.objects.all()
