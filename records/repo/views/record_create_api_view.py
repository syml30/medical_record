from rest_framework.generics import CreateAPIView

from records.views import RecordBaseAPIView


class CreateRecord(RecordBaseAPIView, CreateAPIView):
    pass
