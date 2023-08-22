
import cryptocode


def encrypt_number_card(number):
    key = '6df4eb0333050122c8ed21b896062be7'
    number_encrypt = cryptocode.encrypt(number, key)

    return number_encrypt
