from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from records.models import RecordModel
from records.serializers import RecordModelSerializer


class ListRecordModel(ListAPIView):
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
