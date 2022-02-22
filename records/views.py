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


class CreateRecordModel(CreateAPIView):
    serializer_class = RecordModelSerializer
    queryset = RecordModel.objects.all()
