import uuid
from typing import Any
from django.db import models

CARD_TYPES = (
    ('credit', 'credit'),
    ('debit', 'debit')
)

CREDIT_CARD_FLAGS = (
    ('Visa', 'Visa'),
    ('Mastercard', 'Mastercard'),
    ('Elo', 'Elo'),
    ('Dinners Club', 'Dinners Club'),
    ('American Express', 'American Express')
)


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fancy_name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=20, choices=CARD_TYPES, default=1)
    exp_date = models.DateField()
    holder = models.CharField(max_length=100)
    number = models.CharField(max_length=16)
    cvv = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    flag = models.CharField(
        max_length=20, choices=CREDIT_CARD_FLAGS, default=2)

    def __str__(self):
        return self.fancy_name if self.fancy_name else self.holder
