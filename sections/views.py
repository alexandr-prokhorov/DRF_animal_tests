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
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated,)


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentListAPIView(ListAPIView):
    serializer_class = ContentListSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionContentPaginator


class ContentCreateAPIView(CreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated,)


class ContentUpdateAPIView(UpdateAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class ContentDestroyAPIView(DestroyAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSectionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = QuestionPaginator


class QuestionRetrieveAPIView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        answers = [question.answer for question in Question.objects.all()]
        answer = answers[self.kwargs.get('pk') - 1].strip().lower()
        user_answer = request.data.get('user_answer').strip().lower()
        is_correct = user_answer == answer
        return Response({'is_correct': is_correct})
