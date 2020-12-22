from math import ceil


def classify(number):
    if number <= 0:
        raise ValueError("Number is rejected as it is not a positive integer")
    aliquot_sequence = []
    for divisor in range(1, ceil(number ** 0.5)):
        if number % divisor == 0:
            aliquot_sequence.append(divisor)
            aliquot_sequence.append(number // divisor)
            if number in aliquot_sequence:
                aliquot_sequence.remove(number)
    aliquot_sum = sum(aliquot_sequence)

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    if aliquot_sum < number:
        return "deficient"
