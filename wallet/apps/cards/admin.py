from django.contrib import admin

from wallet.apps.cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
