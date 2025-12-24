from django.contrib import admin
from .models import Category, Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'category', 'author', 'status', 'created_at')
    list_filter = ('status', 'type', 'category', 'created_at')
    search_fields = ('title', 'description', 'author__username', 'author__email')
    list_editable = ('status',)  # Позволяет менять статус прямо из списка (быстрая модерация)
    date_hierarchy = 'created_at'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Автоматически создает slug из имени
