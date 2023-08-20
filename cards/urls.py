from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CardViewSet


router = SimpleRouter()
router.register('cards', CardViewSet)
