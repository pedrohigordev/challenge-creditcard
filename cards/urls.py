from django.urls import path


from .views import CardApiViewCreateAndList, CardApiViewUpdateAndDelete


urlpatterns = [
    path('cards/', CardApiViewCreateAndList.as_view(), name='Cards'),
    path('cards/<str:pk>/', CardApiViewUpdateAndDelete.as_view(), name='Card')
]
