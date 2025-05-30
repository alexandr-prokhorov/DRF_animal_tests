from rest_framework.pagination import PageNumberPagination


class SectionPaginator(PageNumberPagination):
    """
    Пагинатор для секций.
    Устанавливает размер страницы по умолчанию равным 3. Позволяет
    изменять размер страницы через параметр запроса 'page_size',
    с максимальным размером страницы, равным 10.
    """
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class SectionContentPaginator(SectionPaginator):
    """
    Пагинатор для контента секций.
    Устанавливает размер страницы по умолчанию равным 10.
    Наследует настройки от SectionPaginator.
    """
    page_size = 10


class QuestionPaginator(SectionPaginator):
    """
    Пагинатор для вопросов.
    Устанавливает размер страницы по умолчанию равным 5.
    Наследует настройки от SectionPaginator.
    """
    page_size = 5
