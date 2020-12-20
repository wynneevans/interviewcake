import unittest


def get_closing_paren(sentence, opening_paren_index):
    paren_stack = [(opening_paren_index, sentence[opening_paren_index])]

    for i in range(opening_paren_index + 1, len(sentence)):

        previous = paren_stack.pop()
        character = sentence[i]

        if previous[1] == '(' and character == ')':

            if not paren_stack:
                return i

        elif character == ')' or character == '(':
            paren_stack.append(previous)
            paren_stack.append((i, character))

    raise Exception


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)
