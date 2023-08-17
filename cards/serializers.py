from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'number': {'write_only': True},
            'cvv': {'write_only': True}
        }

        model = Card
        fields = {
            'id',
            'fancy_name',
            'type',
            'exp_date',
            'holder',
            'number',
            'cvv',
            'flag'
        }
