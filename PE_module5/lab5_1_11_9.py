# Scenario
# Some say that the Digit of Life is a
# digit evaluated using somebody's birthday.
# It's simple - you just need to sum all the
# digits of the date. If the result contains
# more than one digit, you have to repeat
# the addition until you get exactly one
# digit. For example:
#
#    1 January 2017 = 2017 01 01
#    2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#    1 + 2 = 3
#
# 3 is the digit we searched for and found.


def split(digits):
    return [char for char in digits]


def d_list():
    digits_list = split(digits)
    map_int = map(int, digits_list)
    digits_list = list(map_int)
    return digits_list


digits = ""

while digits != "q":
    digits = input("""
Please enter your date of birth in 8 digits format.
It can be YYYYMMDD, or YYYYDDMM, or MMDDYYYY...
- actually, the order of the digits would not matter... :)
(enter q to quit)
""")

    if digits != "q":

        digits_list = d_list()

        while digits_list:
            number = 0
            for d in digits_list:
                number += d

            if number > 9:
                digits_list = [int(n) for n in str(number)]
            else:
                print(number)
                break
