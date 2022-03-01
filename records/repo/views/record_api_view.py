from records.models import RecordModel
from records.serializers import RecordBaseModelSerializer


class RecordBaseAPIView:
    serializer_class = RecordBaseModelSerializer
    queryset = RecordModel.objects.all()