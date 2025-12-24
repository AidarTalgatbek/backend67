from django.db import models
from django.utils.translation import gettext_lazy as _

class AnnouncementType(models.TextChoices):
    # Оставляем оба для совместимости, но использовать будем FOUND
    LOST = 'LOST', _('Я потерял')
    FOUND = 'FOUND', _('Я нашел')

class AnnouncementStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', _('Активно')
    CLOSED = 'CLOSED', _('Вернулось к владельцу')
    REJECTED = 'REJECTED', _('Отклонено')