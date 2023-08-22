import cryptocode
from creditcard import CreditCard
from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
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

        validated_data['brand'] = brand
        validated_data['number'] = number

        return super().create(validated_data)
