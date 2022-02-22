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
    create_date_time = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user}-{self.data}"
