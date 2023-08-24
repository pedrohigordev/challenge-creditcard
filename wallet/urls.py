from rest_framework.authentication import TokenAuthentication

from django.contrib import admin
from django.urls import include, path


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from wallet.apps.cards.urls import router

from wallet.apps.cards.views import TokenJWTView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Challenge Backend Python Creditcard",
        default_version='v1',
        description="API simples de cadastro de cartões de crédito.",
        contact=openapi.Contact(email="pedrohigor.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    authentication_classes=(TokenAuthentication,),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/token/', TokenJWTView.as_view(), name='token_jwt'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_jwt'),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
