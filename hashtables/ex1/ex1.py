#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    output = []

    """
    YOUR CODE HERE
    """

    for i in range (length):
        hash_table_insert(ht, weights[i], i )

    for weight in weights:

        #special case where the sum of 2 equal weights = limit and one will be overwritten in the linked list 
        if weight == (limit - weight) and weights.count(weight) == 2:
            #find first index
            index1 = weights.index(weight)
            #find 2nd index in the rest of the list
            index2 = weights[index1+1:].index(weight) + index1 + 1

            if index1 > index2:
                output.extend([index1, index2])
            else:
                output.extend([index2, index1])

            return output
             

        index = hash_table_retrieve(ht, weight)

        index_to_find = hash_table_retrieve(ht, limit - weight)

        if index_to_find is not None:
            if index > index_to_find:
                output.append(index)
                output.append(index_to_find)

            #else will find the reverse pair later

    if output:
        return output
    else:    
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")