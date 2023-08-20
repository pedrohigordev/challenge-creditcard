from rest_framework import serializers
from creditcard import CreditCard

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

    def create(self, validated_data):
        number = validated_data['number']

        brand = self.get_card_brand(number)

        validated_data['brand'] = brand

        return super().create(validated_data)

    def get_card_brand(self, card_number):
        card_brand = CreditCard(card_number)

        valid = card_brand.is_valid()

        if valid:
            return card_brand.get_brand()
        else:
            raise serializers.ValidationError(
                'Invalid card number')
