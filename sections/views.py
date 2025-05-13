from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from sections.models import Section, SectionContent
from sections.permissions import IsModerator, IsSuperuser
from sections.serializes.section_serializers import SectionSerializer, SectionListSerializer
from sections.serializes.section_content_serializers import SectionContentSerializer, SectionContentSectionSerializer, \
    SectionContentListSerializer
from sections.paginators import SectionPaginator, SectionContentPaginator


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

class SectionContentListAPIView(ListAPIView):
    serializer_class = SectionContentListSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = SectionContentPaginator

class SectionContentCreateAPIView(CreateAPIView):
    serializer_class = SectionContentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)

class SectionContentRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated,)

class SectionContentUpdateAPIView(UpdateAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)

class SectionContentDestroyAPIView(DestroyAPIView):
    serializer_class = SectionContentSerializer
    queryset = SectionContent.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser | IsModerator)

