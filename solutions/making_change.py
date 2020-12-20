import unittest
import itertools


def achange_possibilities(amount, denominations):
    if len(denominations) == 0:
        return 0

    max_count = amount // denominations[0]
    iter_list = [i for i in range(max_count)]

    ways_of_doing_n_cents = [0] * (amount + 1)
    denomination_counters = [0] * len(denominations)
    # print("w", len(denomination_counters))
    position = 0

    for denomination_counters in itertools.permutations(iter_list, len(denominations)):
        # while True:

        combination_amount = sum(i * j for i, j in zip(denomination_counters, denominations))
        # print(denomination_counters, combination_amount)

        if combination_amount <= amount:
            ways_of_doing_n_cents[combination_amount] += 1
        # if denomination_counters[0]*denominations[0] > amount:
        #    break

        # denomination_counters[position] = 1
        # position = (position + 1) % len(denominations)
        # print(len(denominations), position)

    return ways_of_doing_n_cents[amount]


def change_possibilities(amount, denominations):
    if len(denominations) == 0:
        return 0

    ways_of_doing_n_cents = [0] * (amount + 1)

    ways_of_doing_n_cents[0] = 1

    # using_denominations = [denominations[0]]

    for denomination in denominations:

        for n in range(denomination, amount + 1):
            ways_of_doing_n_cents[n] = ways_of_doing_n_cents[n] + ways_of_doing_n_cents[n - denomination]

    return ways_of_doing_n_cents[amount]


# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
