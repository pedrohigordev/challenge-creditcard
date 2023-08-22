from rest_framework import serializers

from .utils.libs.get_card_brand import get_card_brand
from .utils.libs.encrypt_card_number import encrypt_number_card
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

    def create(self, validated_data):
        number = validated_data['number']

        brand = get_card_brand(number)
        number = encrypt_number_card(number)

        if (not brand != None):
            raise serializers.ValidationError('Card number invalid')

        validated_data['brand'] = brand
        validated_data['number'] = number

        return super().create(validated_data)
