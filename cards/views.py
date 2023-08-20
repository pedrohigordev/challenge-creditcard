from rest_framework import generics

from .models import Card
from .serializers import CardSerializer


class CardApiViewCreateAndList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardApiViewUpdateAndDelete(generics.RetrieveDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
