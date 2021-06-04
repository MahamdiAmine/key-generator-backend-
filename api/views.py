from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from key.models import Key
from key.serializers import KeySerializer


class KeyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = KeySerializer
    queryset = Key.objects.all()
