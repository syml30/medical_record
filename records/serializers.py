from rest_framework.serializers import ModelSerializer
from records.models import RecordModel


class RecordModelSerializer(ModelSerializer):
    class Meta:
        model = RecordModel
        fields = '__all__'
