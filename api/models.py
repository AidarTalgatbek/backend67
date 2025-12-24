from django.db import models
from django.conf import settings
from .choices import AnnouncementType, AnnouncementStatus


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Иконка")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Announcement(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория"
    )

    # Тип объявления (по умолчанию "Я нашел")
    type = models.CharField(
        max_length=10,
        choices=AnnouncementType.choices,
        default=AnnouncementType.FOUND,
        verbose_name="Тип"
    )

    status = models.CharField(
        max_length=20,
        choices=AnnouncementStatus.choices,
        default=AnnouncementStatus.ACTIVE,
        verbose_name="Статус"
    )

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")

    # --- ВАЖНО: Одно фото и телефон прямо здесь ---
    image = models.ImageField(
        upload_to='announcements/',
        blank=True,
        null=True,
        verbose_name="Фото"
    )
    phone = models.CharField(max_length=20, verbose_name="Телефон для связи")
    # ---------------------------------------------

    # Геолокация
    location_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Место")
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    reward = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Вознаграждение"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['-created_at']  # Свежие сверху
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"