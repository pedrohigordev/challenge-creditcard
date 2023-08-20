from rest_framework import viewsets
from rest_framework import mixins

from .models import Card
from .serializers import CardSerializer


class CardViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Card.objects.all()
    serializer_class = CardSerializer
