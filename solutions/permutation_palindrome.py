import unittest
import collections


def ahas_palindrome_permutation(the_string):
    character_dict = collections.defaultdict(int)
    for char in the_string:
        character_dict[char] += 1

    odd_count = 0
    for value in character_dict.values():
        if value % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return True
    else:
        return False


def has_palindrome_permutation(the_string):
    character_set = set()
    for character in the_string:
        if character in character_set:
            character_set.remove(character)
        else:
            character_set.add(character)

    if len(character_set) <= 1:
        return True
    else:
        return False


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
