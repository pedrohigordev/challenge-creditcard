from rest_framework import mixins, viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Card
from .serializers import CardSerializer


class TokenJWTView(TokenObtainPairView):
    pass


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CardViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Card.objects.all()
    serializer_class = CardSerializer
