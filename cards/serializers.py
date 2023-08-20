import calendar
import cryptocode
from creditcard import CreditCard
from rest_framework import serializers
from datetime import datetime

from .models import Card


class ExpDateField(serializers.Field):
    def to_representation(self, value):
        return value.strftime('%m/%Y') if value else None,

    def to_internal_value(self, value):
        try:
            month, year = value.split('/')
            last_day_of_month = calendar.monthrange(int(year), int(month))[1]
            exp_date = datetime(int(year), int(
                month), last_day_of_month).date()

            return exp_date
        except (ValueError, IndexError):
            raise serializers.ValidationError(
                'Invalid date format')


class CardSerializer(serializers.ModelSerializer):
    exp_date = ExpDateField()

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

    def create(self, validated_data):
        number = validated_data['number']

        brand = self.get_card_brand(number)
        number = self.encrypt_number_card(number)
        exp_date_fromated = validated_data['exp_date']

        print(exp_date_fromated)

        validated_data['brand'] = brand
        validated_data['number'] = number
        validated_data['exp_date'] = exp_date_fromated

        return super().create(validated_data)
