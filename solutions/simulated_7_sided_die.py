import random


def rand5():
    return random.randint(1, 5)


def rand7():
    row = rand5() - 1
    column = rand5() - 1

    outcome = row * 5 + column + 1

    while outcome > 21:
        return rand7()

    return outcome % 7 + 1


print('Rolling 7-sided die...')
print(rand7())