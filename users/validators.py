import re
from django.core.exceptions import ValidationError


class PasswordValidator:
    """
    Валидатор для проверки пароля.
    Проверяет, соответствует ли пароль заданному регулярному выражению.
    Пароль должен содержать только латинские буквы и цифры.
    Атрибуты:
    - field: имя поля, для которого выполняется валидация пароля.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg_pattern = re.compile(r'^[A-Za-z0-9]+$')
        tmp_value = dict(value).get(self.field)
        if not bool(reg_pattern.match(tmp_value)):
            raise ValidationError("Пароль должен содержать только латинские буквы и цифры")
