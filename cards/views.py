from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Card
from .serializers import CardSerializer


class CardApiView(APIView):
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
