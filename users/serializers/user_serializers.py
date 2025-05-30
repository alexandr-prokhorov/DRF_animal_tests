from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from users.validators import PasswordValidator


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для представления информации о пользователе.
    Используется для преобразования данных модели User в JSON-формат.
    Включает поля: id, email, last_name, first_name, phone и is_active.
    """

    class Meta:
        model = User
        fields = ['id', 'email', 'last_name', 'first_name', 'phone', 'is_active']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания нового пользователя.
    Включает обязательное поле password с ограничениями по длине.
    Использует PasswordValidator для валидации пароля.
    Метод create создает нового пользователя и устанавливает его пароль.
    """
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=16)

    class Meta:
        model = User
        fields = ['email', 'password']
        validators = [
            PasswordValidator(field='password'),
        ]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления информации о пользователе.
    Позволяет обновлять поля: email, last_name, first_name, password, phone и is_active.
    Закомментированные части кода могут быть использованы для валидации пароля
    и его обновления при необходимости.
    """

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password', 'phone', 'is_active']
    #     validators = [
    #         PasswordValidator(field='password'),
    #     ]
    #
    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance.set_password(password)
    #     instance.save()
    #     return instance


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериализатор для получения токена аутентификации пользователя.
    Расширяет стандартный TokenObtainPairSerializer, добавляя поле email
    в возвращаемый токен.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
