import unittest


def is_valid(code):
    if not code:
        return True

    paren_stack = []

    for i in range(len(code)):
        character = code[i]
        if not paren_stack:
            paren_stack.append((i, character))
            continue

        previous = paren_stack.pop()

        if (previous[1] == '(' and character == ')') or (previous[1] == '[' and character == ']') or (
                previous[1] == '{' and character == '}'):
            continue

        elif character in ['(', ')', '[', ']', '{', '}']:
            paren_stack.append(previous)
            paren_stack.append((i, character))

    return paren_stack == []


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
