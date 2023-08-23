import uuid

from django.db import models


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(max_length=20)
    exp_date = models.DateField()
    holder = models.CharField(max_length=100)
    number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.holder
