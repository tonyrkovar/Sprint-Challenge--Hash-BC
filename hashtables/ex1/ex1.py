#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # find two items who sum of weights equals limit

    # Return a tuple, where the heaviest item is index 0[0]
    # Have a hash table to store values
    # What values should I store in the table?
    # I'm trying to find values that Add up together to equal limit
    # If there is only one value return none
    if len(weights) < 2:
        return None
    index = 0

    limit_remaining = limit
    answer1 = 0
    answer2 = 0

    for i in weights:
        hash_table_insert(ht, i, index)
        index += 1

    for value in weights:
        if (limit_remaining - value) > 0:
            limit_remaining = limit_remaining - value
            answer1 = hash_table_retrieve(ht, value)
        if (limit_remaining - value) == 0:
            if answer1 < value:
                answer1 = hash_table_retrieve(ht, value)

            else:
                answer2 = hash_table_retrieve(ht, value)
    print(answer1, answer2)
    return (answer1, answer2)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
