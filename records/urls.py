from django.urls import path

from records.views import ListRecordModel, RetrieveRecordModel, CreateRecordModel

app_name = 'records'
urlpatterns = [
    path('create', CreateRecordModel.as_view(), name='create'),
    path('retrieve/<int:pk>', RetrieveRecordModel.as_view(), name='retrieve'),
    path('list', ListRecordModel.as_view(), name='list'),
]
