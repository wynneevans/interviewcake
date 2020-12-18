import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    if len(the_list) <= 1:
        return list

    last_list_index = len(the_list) - 1

    for new_index in range(last_list_index):

        random_index = get_random(new_index, last_list_index)

        if random_index != new_index:
            the_list[new_index], the_list[random_index] = the_list[random_index], the_list[new_index]


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
