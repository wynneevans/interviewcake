import unittest


def reverse_words(message):
    left_index = 0
    right_index = len(message) - 1

    while left_index < right_index:
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]

        left_index += 1
        right_index -= 1

    spaces = [i for i, x in enumerate(message) if x == ' ']
    right_indices = [i - 1 for i in spaces]
    left_indices = [i + 1 for i in spaces]
    left_indices.insert(0, 0)
    right_indices.append(len(message) - 1)

    for i in range(len(spaces) + 1):

        left_index = left_indices[i]
        right_index = right_indices[i]

        while left_index < right_index:
            message[left_index], message[right_index] = \
                message[right_index], message[left_index]

            left_index += 1
            right_index -= 1


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
