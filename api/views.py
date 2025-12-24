from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action  # <--- Импортируй это
from rest_framework.response import Response  # <--- Импортируй это
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Announcement
from .serializers import CategorySerializer, AnnouncementSerializer
from .permissions import IsAuthorOrReadOnly


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'type', 'status']
    search_fields = ['title', 'description', 'location_name', 'phone']  # Добавил поиск по телефону
    ordering_fields = ['created_at', 'reward']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # --- ДОБАВЬ ЭТОТ МЕТОД (action) ---
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my(self, request):
        """
        Возвращает объявления только текущего пользователя.
        URL будет: /api/announcements/my/
        """
        # Фильтруем объявления, где автор = текущий юзер
        user_announcements = self.queryset.filter(author=request.user)

        # Сериализуем и отдаем
        serializer = self.get_serializer(user_announcements, many=True)
        return Response(serializer.data)