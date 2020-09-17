from django.urls import path, include
from rest_framework import routers
from .views import LeadViewSet

router = routers.DefaultRouter()
router.register(r'leads', LeadViewSet)
urlpatterns = [
    path('', include(router.urls))
]
