from rest_framework import serializers
from creditcard import CreditCard

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'number': {'write_only': True},
            'cvv': {'write_only': True}
        }
        model = Card
        fields = '__all__'

    def validate_holder(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                'The holder field must have more than 2 characters')
        return value

    def validate_number(self, value):
        card_validate = CreditCard(value)
        valid = card_validate.is_valid()

        if not valid:
            raise serializers.ValidationError(
                'Invalid card number')
        else:
            brand = card_validate.get_brand()

        return value
