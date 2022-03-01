from rest_framework.serializers import ModelSerializer
from records.models import RecordModel


class Record(ModelSerializer):
    class Meta:
        model = RecordModel
        fields = '__all__'
