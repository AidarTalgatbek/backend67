from rest_framework import serializers
from .models import Category, Announcement


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon']


class AnnouncementSerializer(serializers.ModelSerializer):
    # Показываем название категории текстом (удобно для React)
    category_name = serializers.CharField(source='category.name', read_only=True)

    # Автор берется из токена, его нельзя подменить
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Announcement
        fields = [
            'id',
            'author',
            'category',
            'category_name',  # Текстовое название категории
            'type',
            'status',
            'title',
            'description',
            'phone',  # <-- Телефон
            'image',  # <-- Одна картинка (URL)
            'location_name',
            'latitude',
            'longitude',
            'reward',
            'created_at',
            'updated_at'
        ]
        # Эти поля пользователь не может менять вручную
        read_only_fields = ['status', 'created_at', 'updated_at', 'type']

    def create(self, validated_data):
        # Стандартное создание, так как у нас теперь простая модель
        return super().create(validated_data)