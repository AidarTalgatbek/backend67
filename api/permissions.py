from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение:
    - Чтение доступно всем (GET, HEAD, OPTIONS).
    - Изменение/Удаление доступно только автору объекта.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы (чтение) для всех
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешаем изменение только если пользователь — автор объявления
        return obj.author == request.user