from django.contrib import admin
from django.urls import include, path

from wallet.apps.cards.urls import router

from wallet.apps.cards.views import TokenJWTView

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenJWTView.as_view(), name='token_jwt'),
    path('admin/', admin.site.urls)
]
