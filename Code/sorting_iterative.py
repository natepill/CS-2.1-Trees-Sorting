#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n*m) Iterating over given list (n) and also previous values that we
    are continously appending to (m)
    TODO: Memory usage: O(n) By the end of the iteration, prev_values will have length of n because we are
    appending to prev_values n times"""

    prev_values = []

    # Check to see if current value is greater than priors values, if not, then list is not sorted
    for value in items:
        for prev_value in prev_values:
            if value < prev_value:
                return False

        # current values sorted correctly so far
        prev_values.append(value)

    # list is sorted
    return True

    # This is checking if the entire list is sorted, but not efficiently.
    # TODO: Check that all adjacent items are in order, return early if so



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    index_1 = 0
    index_2 = 1

    # Bubble sort until the list is sorted
    while is_sorted(items) == False:
        # if first val is greater than second val:
            #swap the values
        if items[index_1] > items[index_2]:
            temp  = items[index_1]
            items[index_1] = items[index_2]
            items[index_2] = temp
            
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
