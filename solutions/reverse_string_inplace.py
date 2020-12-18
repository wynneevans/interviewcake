def reverse(list_of_chars):
    """
    :param list_of_chars: a string of characters
    :type list_of_chars: str

    """
    left = ''
    right = ''
    for i in range(int(len(list_of_chars) / 2)):
        left = list_of_chars[i]
        right = list_of_chars[-(i + 1)]

        list_of_chars[i] = right
        list_of_chars[-(i + 1)] = left