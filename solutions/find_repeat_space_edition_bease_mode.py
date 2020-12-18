def index(position):
    return position - 1


def find_duplicate(int_list):
    # Find a number that appears more than once ... in O(n) time
    position = len(int_list)
    for _ in range(len(int_list)):
        position = int_list[index(position)]

    cycle_length = 1
    start_position = position
    position = int_list[index(position)]
    while position != start_position:
        position = int_list[index(position)]
        cycle_length += 1

    position = len(int_list)
    stick_position = len(int_list)

    for _ in range(cycle_length):
        stick_position = int_list[index(stick_position)]

    while position != stick_position:
        position = int_list[index(position)]
        stick_position = int_list[index(stick_position)]

    return stick_position