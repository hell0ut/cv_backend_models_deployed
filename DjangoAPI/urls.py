from django.urls import path,include
from .views import ImageViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cats_vs_dogs',ImageViewSet)


urlpatterns = [
    path('',include(router.urls)),
]