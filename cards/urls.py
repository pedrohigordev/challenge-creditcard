from django.urls import path


from .views import CardApiView


urlpatterns = [
    path('cards/', CardApiView.as_view(), name='Cards')
]
