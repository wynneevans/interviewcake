import unittest


def kth_to_last_node(k, head):
    if k < 1:
        raise Exception

    node = head
    list_len = 0
    while node:
        node = node.next
        list_len += 1

    kth_last = list_len - k

    if kth_last < 0:
        raise Exception

    node = head

    for _ in range(kth_last):
        node = node.next

    return node


# Tests

class Test(unittest.TestCase):
    class LinkedListNode(object):

        def __init__(self, value, next_value=None):
            self.value = value
            self.next = next_value

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)
