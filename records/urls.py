from django.urls import path

from records.views import ListRecordModel, RetrieveRecordModel, CreateRecordModel

app_name = "records"
urlpatterns = [
    path('list_record', ListRecordModel.as_view(), name='list_record'),
    path('retrieve_record/<int:pk>', RetrieveRecordModel.as_view(), name='retrieve_record'),
    path('create_record', CreateRecordModel.as_view(), name='create_record'),
]
