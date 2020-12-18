def get_permutations(string):
    if len(string) < 2:
        return {string}

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
