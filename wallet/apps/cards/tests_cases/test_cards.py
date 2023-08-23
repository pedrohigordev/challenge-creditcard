
from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Card

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status


class CardTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username='phsousa', password='123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.key)

        self.card_data = {
            'exp_date': '2023-12-31',
            'holder': 'Pedro Sousa',
            'number': '4539578763621486',
            'cvv': 555,
        }

    def test_authentication(self):
        credentials = {
            "username": "phsousa",
            "password": "123"
        }

        response = self.client.post(
            '/api/v1/token/', credentials, format='json')

        token = response.data.get('access')

        if token:
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
            response = self.client.get('/api/v1/cards/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        else:
            print('Token not found')

    # def test_create_card(self):
    #     self.assertEqual(self.card.holder, 'Pedro Sousa')
    #     self.assertEqual(self.card.cvv, 555)
