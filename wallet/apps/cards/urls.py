from rest_framework.routers import SimpleRouter

from .views import CardViewSet, TokenJWTView

router = SimpleRouter()
router.register('cards', CardViewSet)
