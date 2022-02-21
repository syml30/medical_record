from django.db import models


class RecordModel(models.Model):
    user = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    data = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
