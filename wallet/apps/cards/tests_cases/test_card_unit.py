import uuid
from django.test import TestCase
from datetime import date
from ..models import Card


class CardModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.card_data = {
            'brand': 'visa',
            'exp_date': date(2023, 12, 31),
            'holder': 'Pedro Sousa',
            'number': '4539578763621486',
            'cvv': 555,
        }

    def test_card_creation(self):
        card = Card.objects.create(**self.card_data)
        self.assertEqual(card.brand, 'visa')
        self.assertEqual(card.exp_date, date(2023, 12, 31))
        self.assertEqual(card.holder, 'Pedro Sousa')
        self.assertEqual(card.number, '4539578763621486')
        self.assertEqual(card.cvv, 555)
        self.assertIsNotNone(card.created_at)
        self.assertIsInstance(card.id, uuid.UUID)

    def test_card_str_representation(self):
        card = Card.objects.create(**self.card_data)
        self.assertEqual(str(card), 'Pedro Sousa')

    def test_card_list(self):
        Card.objects.create(**self.card_data)

        cards = Card.objects.all()

        self.assertEqual(len(cards), 1)
