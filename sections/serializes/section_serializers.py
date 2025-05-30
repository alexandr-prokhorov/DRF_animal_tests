from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, Content
from sections.serializes.content_serializers import ContentSectionSerializer


class SectionSerializer(ModelSerializer):
    """
    Сериализатор для модели Section.
    Этот сериализатор используется для преобразования экземпляров модели Section
    в JSON-формат и обратно. Он включает все поля модели.
    """

    class Meta:
        model = Section
        fields = '__all__'


class SectionListSerializer(ModelSerializer):
    """
    Сериализатор для списка секций с содержимым.
    Включает идентификатор, заголовок секции и список заголовков контента,
    связанных с данной секцией. Поле section_content_title заполняется
    с помощью метода get_section_content_title, который возвращает
    сериализованные данные контента, относящегося к секции.
    """
    section_content_title = SerializerMethodField()

    def get_section_content_title(self, section):
        return ContentSectionSerializer(Content.objects.filter(section=section), many=True).data

    class Meta:
        model = Section
        fields = ('id', 'title', 'section_content_title')
