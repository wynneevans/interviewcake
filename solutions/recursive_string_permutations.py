import unittest


def get_permutations(string):
    if len(string) < 2:
        return {string}  # set([string])

    string_1 = string[:-1]
    string_2 = string[-1]

    permutations_except_last = get_permutations(string_1)

    # Generate all permutations of the input string
    permutations = set()
    for permutation_except_last in permutations_except_last:
        for position in range(len(string_1) + 1):
            permutation = permutation_except_last[:position] + string_2 + permutation_except_last[position:]
            permutations.add(permutation)

    return permutations


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = {''}
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = {'a'}
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = {'ab', 'ba'}
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
