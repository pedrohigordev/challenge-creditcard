import calendar
import cryptocode
from creditcard import CreditCard
from rest_framework import serializers
from datetime import datetime

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'brand': {'read_only': True},
        }
        model = Card
        fields = '__all__'

    def validate_holder(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                'The holder field must have more than 2 characters')
        return value

    def get_card_brand(self, card_number):
        card_brand = CreditCard(card_number)

        valid = card_brand.is_valid()

        if valid:
            return card_brand.get_brand()
        else:
            raise serializers.ValidationError(
                'Invalid card number')

    def encrypt_number_card(self, number):
        key = '6df4eb0333050122c8ed21b896062be7'
        number_encrypt = cryptocode.encrypt(number, key)

        return number_encrypt

    def format_exp_date(self, exp_date):
        year = exp_date.year
        month = exp_date.month
        last_day_of_month = calendar.monthrange(year, month)[1]
        formatted_date = datetime(
            year, month, last_day_of_month).strftime('%Y-%m-%d')
        return formatted_date

    def create(self, validated_data):
        number = validated_data['number']

        brand = self.get_card_brand(number)
        number = self.encrypt_number_card(number)

        validated_data['brand'] = brand
        validated_data['number'] = number

        exp_date = validated_data.get('exp_date')
        exp_date_formatted = self.format_exp_date(exp_date)
        validated_data['exp_date'] = exp_date_formatted

        return super().create(validated_data)
