from rest_framework.generics import RetrieveAPIView

from records.views import RecordBaseAPIView


class RetrieveRecord(RecordBaseAPIView, RetrieveAPIView):
    lookup_field = 'pk'
