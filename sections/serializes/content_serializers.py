from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Section, Content


class ContentSerializer(ModelSerializer):
    """
    Сериализатор для модели Content.
    Этот сериализатор используется для преобразования экземпляров модели Content
    в JSON-формат и обратно.
    """

    class Meta:
        model = Content
        fields = '__all__'


class ContentSectionSerializer(ModelSerializer):
    """
    Сериализатор для модели Content, ограниченный полями id и title.
    Этот сериализатор используется для получения упрощенной информации о контенте,
    включая только идентификатор и заголовок.
    """

    class Meta:
        model = Content
        fields = ('id', 'title',)


class ContentListSerializer(ModelSerializer):
    """
    Сериализатор для списка контента с привязкой к секции.
    Этот сериализатор используется для отображения списка контента,
    включая идентификатор, секцию (по заголовку) и заголовок контента.
    """
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Content
        fields = ('id', 'section', 'title',)
