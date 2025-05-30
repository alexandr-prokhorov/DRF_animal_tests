from django.contrib import admin
from sections.models import Section, Content, Question


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления секциями.
    Позволяет отображать идентификатор и заголовок секции в списке,
    а также фильтровать секции по заголовку. Сортировка осуществляется
    по идентификатору.
    """
    list_display = ('id', 'title')
    list_filter = ('title',)
    ordering = ('id',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления контентом.
    Позволяет отображать идентификатор, секцию и заголовок контента в списке,
    а также фильтровать контент по секции. Сортировка осуществляется
    по идентификатору и секции.
    """
    list_display = ('id', 'section', 'title')
    list_filter = ('section',)
    ordering = ('id', 'section')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Админ-класс для управления вопросами.
    Позволяет отображать идентификатор, секцию вопроса, текст вопроса,
    описание и ответ в списке, а также фильтровать вопросы по секции.
    Сортировка осуществляется по идентификатору и секции вопроса.
    """
    list_display = ('id', 'question_section', 'question', 'description', 'answer')
    list_filter = ('question_section',)
    ordering = ('id', 'question_section')
