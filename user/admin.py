from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админ-панель пользователя"""
    list_display = ('pk', 'email', 'phone',
                    'country', 'city', 'avatar')
