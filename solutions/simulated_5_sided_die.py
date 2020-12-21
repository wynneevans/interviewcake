import random


def rand7():
    return random.randint(1, 7)


def rand5():
    result = 7
    while result > 5:
        result = rand7()

    return result


print('Rolling 5-sided die...')
print(rand5())