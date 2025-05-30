from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления пользователями.
    Позволяет отображать в списке пользователей поля id, email, last_name и first_name.
    Позволяет делать ссылки на редактирование по полям id и email.
    Сортировка пользователей осуществляется по идентификатору.
    """
    list_display = ('id', 'email', 'last_name', 'first_name')
    list_display_links = ('id', 'email')
    ordering = ('id',)
