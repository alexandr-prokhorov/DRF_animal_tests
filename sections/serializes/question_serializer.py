from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField

from sections.models import Question, Section


class QuestionSectionSerializer(ModelSerializer):
    """
    Сериализатор для модели Question, включающий только идентификатор и секцию вопроса.
    Поле question_section отображается через SlugRelatedField с использованием поля
    'title' модели Section, что позволяет выводить название секции вместо идентификатора.
    """
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'question_section')


class QuestionSerializer(ModelSerializer):
    """
    Полный сериализатор для модели Question.
    Включает идентификатор, секцию вопроса (отображаемую по названию секции через SlugRelatedField)
    и текст вопроса.
    """
    question_section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'question_section', 'question')
