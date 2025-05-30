from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """
    Класс для определения ролей пользователей.
    Использует TextChoices для создания перечисления ролей:
    - MEMBER: обычный пользователь
    - MODERATOR: модератор
    """
MEMBER = 'member', _('member')
MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """
    Модель пользователя, расширяющая стандартную модель AbstractUser .
    Поля:
    - email: уникальный адрес электронной почты пользователя.
    - role: роль пользователя (MEMBER или MODERATOR).
    - first_name: имя пользователя.
    - last_name: фамилия пользователя.
    - phone: номер телефона пользователя.
    - is_active: статус активности пользователя.
    Использует email в качестве поля для аутентификации (USERNAME_FIELD).
    """
    username = None
    email = models.EmailField(unique=True, verbose_name=_('email address'))
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    first_name = models.CharField(max_length=50, verbose_name=_('first name'), **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name=_('last name'), **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name=_('phone number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['id']
