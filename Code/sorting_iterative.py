#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Iterating over given list (n), just incrementing indicies and comparing values
    TODO: Memory usage: O(1) No extra space allocated expect for some variables that are being incremented"""

    index_1 = 0
    index_2 = 1

    while index_2 < len(items)-1:
        # out of order
        if items[index_2] < items[index_1]:
            return False
        # currently in order
        else:
            index_1 += 1
            index_2 += 1

    return True

    # Frist Version
    # prev_values = []
    #
    # # Check to see if current value is greater than priors values, if not, then list is not sorted
    # for value in items:
    #     for prev_value in prev_values:
    #         if value < prev_value:
    #             return False
    #
    #     # current values sorted correctly so far
    #     prev_values.append(value)
    #
    # # list is sorted
    # return True

    # TODO: Check that all adjacent items are in order, return early if so



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n*m), Worst cast is O(n^2) If the entire list is out of order, then we would have to do bubble sort (n)
    times for (n) values in the list. Additional O(n) to check if sorted
    TODO: Memory usage: O(1) because we just allocated memory for a couple variables"""

    index_1 = 0
    index_2 = 1

    # TODO: keep counter for swaps for early exit

    # Bubble sort until the list is sorted
    while is_sorted(items) == False:
        # print("Still not sorted")

        while index_2 < len(items)-1:

            # if first val is greater than second val:
                #swap the values
            if items[index_1] > items[index_2]: # O(1)
                temp  = items[index_1]
                items[index_1] = items[index_2]
                items[index_2] = temp

            # comparing next 2 values in the list
            index_1 += 1
            index_2 += 1

        # reset indicies for begining iterations
        index_1 = 0
        index_2 = 1

    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n*m) Best case O(n) with only a few swaps, but could be O(n^2) if values
    at every position need to be swapped
    Memory usage: O(1) Not really allocating much memory besides for variables """

    # init curr_index
    # init swap_index, value
    # Selection sort until the list is_sorted
        # find the smallest value in the list from the current index until swap index has reach end of list
            # update swap_value with smallest value

            # increment swap_index
        # swap value at curr_index with value at swap_index
        # increment curr_index
        # reset swap_index to curr_index + 1 and swap value to list value at curr_index+1

    # iterate over range of indicies
    for index in range(len(items)):

        # find the smallest value in the list from the current index
        smallest_index = index
        # iterate over range of indicies from current index to end of list
        for small_index in range(index+1, len(items)):
            if items[smallest_index] > items[small_index]:
                smallest_index = small_index

        # Swap current index with smallest element
        items[index], items[smallest_index] = items[smallest_index], items[index]



    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # iterate over range of indicies

    # compare the value of current index with preceding values at prior indicies
    # insert current value at index whose value is smaller than current value

    # Skip first index in index iteration range because first value is "sorted"
    for index in range(1, len(items)):
        # Iterate over preceding indicies
        for prev_index in range(index, -1, -1):
            # Point of insertion
            if items[index] > items[prev_index]:
                items.insert(index, items[index])

        # No more values to compare to, so current value is the smallest value seen so far
        if items[index] < items[0]:
            items.insert(0, items[index])


        # while index > 0 or items[index-1] > items[index]:
        #     if items[index] < items[insert_index]:
        #         index -= 1

        #
        # insert_index = index-1
        # # Keep comparing until reached begining of list
        # while index > 0:
        #
        #     if items[index] < items[insert_index]:


    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    pass


if __name__ == "__main__":
    # items = [1,3,2,1]
    # items = [1,2,3,4]
    items = [1, 2, 3, 1, 2, 5]
    print(is_sorted(items))
    selection_sort(items)
    print(is_sorted(items))
    print(items)
