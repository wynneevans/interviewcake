import unittest


def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers
    # initialize first 3 numbers as largest 3 numbers
    # iterate through rest of list
    # replace one of the 3 numbers if current number is in top 3

    if len(list_of_ints) < 3:
        raise ValueError('List has less than 3 elements.')

    top_three = [list_of_ints[0], list_of_ints[1], list_of_ints[2]]
    bottom_three = [list_of_ints[0], list_of_ints[1], list_of_ints[2]]

    for i in range(3, len(list_of_ints)):
        current_int = list_of_ints[i]
        if any(current_int > i for i in top_three):
            top_three[top_three.index(min(top_three))] = current_int
        if any(current_int < i for i in bottom_three):
            bottom_three[bottom_three.index(max(bottom_three))] = current_int

    bottom_two = sorted(bottom_three)[:2]

    if max(top_three) < 0:
        return top_three[0] * top_three[1] * top_three[2]
    elif all(i < 0 for i in bottom_two):
        return max(bottom_two[0] * bottom_two[1] * max(top_three), top_three[0] * top_three[1] * top_three[2])
    else:
        return top_three[0] * top_three[1] * top_three[2]


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
