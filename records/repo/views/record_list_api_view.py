from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from records.views import RecordBaseAPIView


class ListRecord(RecordBaseAPIView, ListAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', ]
    search_fields = ['^user', ]
    ordering_fields = ['user', ]
