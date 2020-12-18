import unittest


def find_repeat(numbers):
    # print("numbers are: ", numbers)

    # Find a number that appears more than once
    # There always has to be at least one duplicate

    floor = 1
    ceiling = len(numbers)

    while floor < ceiling:

        distance = ceiling - floor
        half_distance = distance // 2
        mid_value = floor + half_distance

        if distance == 1:
            return mid_value

        count = 0
        for number in numbers:
            # if number >= floor and number < mid_value:
            if floor <= number < mid_value:
                count += 1

        # print(floor, ceiling, distance, half_distance, mid_value, count)

        if count > half_distance:
            ceiling = mid_value
        else:
            floor = mid_value

    return None


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
