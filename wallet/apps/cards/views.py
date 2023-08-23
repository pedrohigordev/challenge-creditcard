from rest_framework import mixins, viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Card
from .serializers import CardSerializer


class TokenJWTView(TokenObtainPairView):
    pass


class CardViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
