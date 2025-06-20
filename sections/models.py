from django.db import models
from users.models import NULLABLE
from django.utils.translation import gettext_lazy as _


class Section(models.Model):
    """
    Модель для представления секции.
    Секция содержит заголовок и описание. Заголовок является обязательным полем,
    а описание может быть пустым. Секции сортируются по идентификатору.
    """
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"), **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")
        ordering = ['id']


class Content(models.Model):
    """
    Модель для представления контента, связанного с секцией.
    Контент содержит ссылку на секцию, заголовок и текст контента. Заголовок
    является обязательным полем, а текст контента может быть пустым. Контент
    сортируется по идентификатору.
    """
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_("Section"))
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _("Section Content")
        verbose_name_plural = _("Section Contents")
        ordering = ['id']


class Question(models.Model):
    """
    Модель для представления вопроса, связанного с секцией.
    Вопрос содержит ссылку на секцию, описание, текст вопроса и ответ. Описание,
    текст вопроса и ответ могут быть пустыми. Вопросы сортируются по секции.
    """
    question_section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_("Section"))
    description = models.TextField(verbose_name=_("Description"), **NULLABLE)
    question = models.TextField(verbose_name=_("Question"), **NULLABLE)
    answer = models.CharField(max_length=40, verbose_name=_("Answer"), **NULLABLE)

    def __str__(self):
        return f'Вопрос по курсу {self.question_section.title}'

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['question_section']
