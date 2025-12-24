from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AnnouncementViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]