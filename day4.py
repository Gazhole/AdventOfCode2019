"""
Advent of Code 2019
Day 4
"""


def check_adjacent_digits_present(password):
    password = "".join(password)
    results = dict()
    digits = [str(i) for i in range(0, 10)]

    for digit in digits:
        chklist = [str(digit * x) for x in range(2, 7)]

        for chk in chklist:
            if chk in password:
                results[digit] = chk

    chains = results.values()

    double = False
    triple = False

    for chain in chains:
        if len(chain) == 2:
            double = True
        elif len(chain) > 2:
            triple = True

    if double and triple:
        return True
    elif double and not triple:
        return True
    elif triple and not double:
        return False
    else:
        return False


def check_values_dont_decrease(password):
    if password[0] <= password[1] <= password[2] <= password[3] <= password[4] <= password[5]:
        return True
    else:
        return False


def main():
    to_test = [list(str(password)) for password in range(108457, 562041)]
    good_passwords = list()

    for password in to_test:
        if len(password) == 6 and check_adjacent_digits_present(password) and check_values_dont_decrease(password):
            good_passwords.append(password)
        else:
            continue

    print(len(good_passwords))


if __name__ == "__main__":
    main()
