import unittest


def index(position):
    return position - 1


def find_duplicate(int_list):
    # Find a number that appears more than once ... in O(n) time
    position = len(int_list)
    for _ in range(len(int_list)):
        position = int_list[index(position)]

    cycle_length = 1
    start_position = position
    position = int_list[index(position)]
    while position != start_position:
        position = int_list[index(position)]
        cycle_length += 1

    position = len(int_list)
    stick_position = len(int_list)

    for _ in range(cycle_length):
        stick_position = int_list[index(stick_position)]

    while position != stick_position:
        position = int_list[index(position)]
        stick_position = int_list[index(stick_position)]

    return stick_position


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_duplicate([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_duplicate([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_duplicate([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
