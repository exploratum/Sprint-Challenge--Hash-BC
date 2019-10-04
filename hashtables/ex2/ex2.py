#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    #save tickets in linked list
    for ticket in tickets:

        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # first destination
    destination = hash_table_retrieve(hashtable, "NONE")
    route[0] = destination
    source = destination

    # subsequent destinations
    for i in range(1, length):
        destination = hash_table_retrieve(hashtable, source)
        route[i] = destination
        source = destination


    while source is not "NONE":
        destination = hash_table_retrieve(hashtable, source)
        route.append(destination)
        source = destination
    
    return route
