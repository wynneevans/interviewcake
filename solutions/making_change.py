def change_possibilities(amount, denominations):
    if len(denominations) == 0:
        return 0

    ways_of_doing_n_cents = [0] * (amount + 1)

    ways_of_doing_n_cents[0] = 1

    # using_denominations = [denominations[0]]

    for denomination in denominations:

        for n in range(denomination, amount + 1):
            ways_of_doing_n_cents[n] = ways_of_doing_n_cents[n] + ways_of_doing_n_cents[n - denomination]

    return ways_of_doing_n_cents[amount]
