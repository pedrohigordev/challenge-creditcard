from creditcard import CreditCard


def get_card_brand(card_number):
    card_object = CreditCard(card_number)

    if card_object.is_valid():
        return card_object.get_brand()
    else:
        return None
