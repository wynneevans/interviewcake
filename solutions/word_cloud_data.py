import unittest


class WordCloudData(object):

    def __init__(self, input_string):

        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def add_word_to_dictionary(self, word):
        word = word.lower()
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1
        else:
            self.words_to_counts[word] = 1

    def populate_words_to_counts(self, input_string):

        left_index = 0
        right_index = 0

        for i, character in enumerate(input_string):
            # print(character)
            if character == " ":
                if input_string[i - 1].isalpha():
                    right_index = i
                    self.add_word_to_dictionary(input_string[left_index:right_index])
                    left_index = i + 1
                else:
                    right_index = i - 1
                    self.add_word_to_dictionary(input_string[left_index:right_index])
                    left_index = i + 1
            elif i == len(input_string) - 1:
                if input_string[i].isalpha():
                    self.add_word_to_dictionary(input_string[left_index:])
                else:
                    self.add_word_to_dictionary(input_string[left_index:-1])

            # print(input_string[left_index:right_index+1].lower())
            # self.words_to_counts[input_string[left_index:right_index+1].lower()]


# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'i': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'strawberry': 1, 'short': 1, 'yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"bakery": 1, "cakes": 1, "allie's": 1, "sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
