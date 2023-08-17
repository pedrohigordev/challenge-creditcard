from django.db import models


CARD_TYPES = (
    ('1', 'credit'),
    ('2', 'debit')
)

CREDIT_CARD_FLAGS = (
    ('1', 'Visa'),
    ('2', 'Mastercard'),
    ('3', 'Elo'),
    ('4', 'Dinners Club'),
    ('5', 'American Express')
)


class Card(models.Model):
    fancy_name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=20, choices=CARD_TYPES, default=1)
    exp_date = models.DateField()
    holder = models.CharField(max_length=100)
    number = models.CharField(max_length=16)
    cvv = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    flag = models.CharField(
        max_length=20, choices=CREDIT_CARD_FLAGS, default=2)

    def __str__(self) -> str:
        return self.fancy_name if self.fancy_name else self.holder
