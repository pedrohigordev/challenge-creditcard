from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib import admin
from django.urls import include, path


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from wallet.apps.cards.urls import router

from wallet.apps.cards.views import TokenJWTView

schema_view = get_schema_view(
    openapi.Info(
        title="Challenge Backend Python Creditcard",
        default_version='v1',
        description="API simples de cadastro de cartões de crédito.",
        contact=openapi.Contact(email="pedrohigor.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(JWTAuthentication,),
)


urlpatterns = [
    path('api/v1/token/', TokenJWTView.as_view(), name='token_jwt'),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger'),
]
