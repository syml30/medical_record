from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from records.models import RecordModel
from records.serializers import RecordModelSerializer


class CreateRecordModel(CreateAPIView):
    serializer_class = RecordModelSerializer
    queryset = RecordModel.objects.all()


class RetrieveRecordModel(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = RecordModelSerializer
    queryset = RecordModel.objects.all()


class ListRecordModel(ListAPIView):
    serializer_class = RecordModelSerializer
    queryset = RecordModel.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', ]
    search_fields = ['^user', ]
    ordering_fields = ['user', ]
