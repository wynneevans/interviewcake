import unittest


def get_max_profit(stock_prices):
    # Calculate the max profit
    if len(stock_prices) < 2:
        raise Exception

    # need to find a low number followed by a high number

    max_profit = stock_prices[1] - stock_prices[0]
    min_price = stock_prices[0]

    for i in range(1, len(stock_prices)):
        current_price = stock_prices[i]

        max_profit = max(max_profit, current_price - min_price)

        min_price = min(min_price, current_price)

    return max_profit


# Tests

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
