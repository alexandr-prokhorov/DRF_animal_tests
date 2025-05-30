from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers.user_serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, \
    UserTokenObtainPairSerializer


class UserListAPIView(ListAPIView):
    """
    Представление для получения списка пользователей.
    Использует сериализатор UserSerializer для преобразования данных
    пользователей в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserCreateAPIView(CreateAPIView):
    """
    Представление для создания нового пользователя.
    Использует сериализатор UserCreateSerializer для валидации и создания
    нового пользователя. Доступ к этому представлению разрешен только
    аутентифицированным пользователям.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (IsAuthenticated,)


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Представление для получения информации о конкретном пользователе.
    Использует сериализатор UserSerializer для преобразования данных
    пользователя в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления информации о пользователе.
    Использует сериализатор UserUpdateSerializer для валидации и обновления
    существующего пользователя. Доступ к этому представлению разрешен только
    аутентифицированным пользователям. Возвращает только информацию о текущем пользователе.
    """
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления пользователя.
    Доступ к этому представлению разрешен только аутентифицированным пользователям.
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserTokenObtainPairView(TokenObtainPairView):
    """
    Представление для получения токена аутентификации пользователя.
    Использует сериализатор UserTokenObtainPairSerializer для получения
    токена доступа и обновления.
    """
    serializer_class = UserTokenObtainPairSerializer
