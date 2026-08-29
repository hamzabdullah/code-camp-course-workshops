def verify_card_number(card_number):
    card_number = card_number.replace("-", "").replace(" ", "")

    digits = [int(digit) for digit in card_number]

    total = 0
    reverse_digits = digits[::-1]

    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2

            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"