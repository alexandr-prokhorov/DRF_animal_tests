from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, Content, Question
from sections.permissions import IsModerator
from sections.serializes.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializes.content_serializers import ContentSerializer, ContentListSerializer
from sections.serializes.question_serializer import QuestionSerializer, QuestionSectionSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator, QuestionPaginator


class SectionListAPIView(ListAPIView):
    """
    Представление для получения списка секций.
    Использует сериализатор SectionListSerializer для преобразования данных
    секций в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям. Пагинация осуществляется с помощью
    SectionPaginator.
    """
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    """
    Представление для создания новой секции.
    Использует сериализатор SectionSerializer для валидации и создания
    новой секции. Доступ к этому представлению разрешен только
    аутентифицированным пользователям с ролями администратора или модератора.
    """
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionRetrieveAPIView(RetrieveAPIView):
    """
    Представление для получения информации о конкретной секции.
    Использует сериализатор SectionSerializer для преобразования данных
    секции в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям.
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления информации о секции.
    Использует сериализатор SectionSerializer для валидации и обновления
    существующей секции. Доступ к этому представлению разрешен только
    аутентифицированным пользователям с ролями администратора или модератора.
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления секции.
    Использует сериализатор SectionSerializer для удаления существующей
    секции. Доступ к этому представлению разрешен только
    аутентифицированным пользователям с ролями администратора или модератора.
    """
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentListAPIView(ListAPIView):
    """
    Представление для получения списка контента секций.
    Использует сериализатор ContentListSerializer для преобразования данных
    контента в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям. Пагинация осуществляется с помощью
    SectionContentPaginator.
    """
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionContentPaginator


class ContentCreateAPIView(CreateAPIView):
    """
    Представление для создания нового контента.
    Использует сериализатор ContentSerializer для валидации и создания
    нового контента. Доступ к этому представлению разрешен только
    аутентифицированным пользователям с ролями администратора или модератора.
    """
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentRetrieveAPIView(RetrieveAPIView):
    """
    Представление для получения информации о конкретном контенте.
    Использует сериализатор ContentSerializer для преобразования данных
    контента в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям.
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    """
    Представление для обновления информации о контенте.
    Использует сериализатор ContentSerializer для валидации и обновления
    существующего контента. Доступ к этому представлению разрешен только
    аутентифицированным пользователям с ролями администратора или модератора.
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentDestroyAPIView(DestroyAPIView):
    """
    Представление для удаления контента.
    Использует сериализатор ContentSerializer для удаления существующего
    контента. Доступ к этому представлению разрешен только
    аутентифицированным пользователям с ролями администратора или модератора.
    """
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class QuestionListAPIView(ListAPIView):
    """
    Представление для получения списка вопросов.
    Использует сериализатор QuestionSectionSerializer для преобразования данных
    вопросов в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям. Пагинация осуществляется с помощью
    QuestionPaginator.
    """
    serializer_class = QuestionSectionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator


class QuestionRetrieveAPIView(RetrieveAPIView):
    """
    Представление для получения информации о конкретном вопросе.
    Использует сериализатор QuestionSerializer для преобразования данных
    вопроса в JSON-формат. Доступ к этому представлению разрешен только
    аутентифицированным пользователям.
    Также обрабатывает POST-запрос для проверки ответа пользователя на вопрос.
    Возвращает информацию о том, является ли ответ пользователя правильным.
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].strip().lower()
        user_answer = request.data.get('user_answer').strip().lower()
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
