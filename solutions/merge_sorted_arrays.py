import unittest


def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list + alices_list)
    merged_list = [None] * merged_list_size

    index_of_my_list = 0
    index_of_alices_list = 0
    index_of_merged_list = 0

    while index_of_merged_list < merged_list_size:
        is_my_list_exhausted = index_of_my_list >= len(my_list)
        is_alices_list_exhausted = index_of_alices_list >= len(alices_list)

        if (not is_alices_list_exhausted and (
                is_my_list_exhausted or my_list[index_of_my_list] > alices_list[index_of_alices_list])):
            merged_list[index_of_merged_list] = alices_list[index_of_alices_list]
            index_of_alices_list += 1
        elif (not is_my_list_exhausted and (
                is_alices_list_exhausted or my_list[index_of_my_list] < alices_list[index_of_alices_list])):
            merged_list[index_of_merged_list] = my_list[index_of_my_list]
            index_of_my_list += 1

        index_of_merged_list += 1

    return merged_list


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
