import calendar
from datetime import datetime
from rest_framework import serializers

from .utils.libs.get_card_brand import get_card_brand
from .utils.libs.encrypt_card_number import encrypt_number_card
from .models import Card


class ExpDateField(serializers.Field):
    def validate_date(self, date):
        today = datetime.now().date()

        received_date = datetime.strptime(date, '%Y-%m-%d').date()

        if (received_date < today):
            raise ValueError(
                "Data is not in the format: DD/YYYY or is less than current data")

        return date

    def to_representation(self, validate_data):
        return validate_data

    def to_internal_value(self, date):

        try:
            month, year = date.split('/')
            last_day_of_month = calendar.monthrange(int(year), int(month))[1]

            date_formated = f'{year}-{month}-{last_day_of_month}'

            self.validate_date(date_formated)

            return date_formated

        except ValueError:
            raise serializers.ValidationError(
                'Data is not in the format: DD/YYYY or is less than current data', )


class CardSerializer(serializers.ModelSerializer):
    exp_date = ExpDateField()

    class Meta:
        extra_kwargs = {
            'brand': {'read_only': True},
        }
        model = Card
        fields = (
            'id',
            'brand',
            'exp_date',
            'holder',
            'number',
            'cvv'
        )

    def validate_cvv(self, value):
        if 3 > int(value) < 4:
            raise serializers.ValidationError(
                'The CVV must have 3 to 4 characters')

        return value

    def validate_holder(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                'The holder field must have more than 2 characters')
        return value

    def create(self, validated_data):
        number = validated_data['number']

        brand = get_card_brand(number)
        number = encrypt_number_card(number)

        if (not brand != None):
            raise serializers.ValidationError('Card number invalid')

        validated_data['brand'] = brand
        validated_data['number'] = number

        return super().create(validated_data)
