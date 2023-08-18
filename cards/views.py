from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Card
from .serializers import CardSerializer


class CardApiView(APIView):
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Created"}, status=status.HTTP_201_CREATED)
