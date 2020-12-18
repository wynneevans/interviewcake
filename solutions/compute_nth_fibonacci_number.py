import unittest


class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):

        if n == 0 or n == 1:
            return n

        if n in self.memo:
            return self.memo[n]

        else:
            result = self.fib(n - 1) + self.fib(n - 2)
            self.memo[n] = result
            return result


# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = Fibber().fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = Fibber().fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = Fibber().fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = Fibber().fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = Fibber().fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = Fibber().fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            Fibber.fib(-1)


unittest.main(verbosity=2)
