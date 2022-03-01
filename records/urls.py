from django.urls import path

from records.views import *

app_name = 'records'
urlpatterns = [
    path('create', RecordCreateAPIView.as_view(), name='create'),
    path('retrieve/<int:pk>', RecordRetrieveAPIView.as_view(), name='retrieve'),
    path('list', RecordListAPIView.as_view(), name='list'),
]
