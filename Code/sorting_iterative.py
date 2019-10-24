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
    TODO: Running time: O(n^2) If the entire list is out of order, then we would have to do bubble sort (n)
    times for (n) values in the list
    TODO: Memory usage: O(1) because we just allocated memory for a couple variables"""

    index_1 = 0
    index_2 = 1

    # Bubble sort until the list is sorted
    while is_sorted(items) == False:
        # print("Still not sorted")

        while index_2 < len(items)-1:

            # if first val is greater than second val:
                #swap the values
            if items[index_1] > items[index_2]:
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # init curr_index
    # init swap_index, value
    # Selection sort until the list is_sorted
        # find the smallest value in the list from the current index until swap index has reach end of list
            # update swap_value with smallest value

            # increment swap_index
        # swap value at curr_index with value at swap_index
        # increment curr_index
        # reset swap_index to curr_index + 1 and swap value to list value at curr_index+1

    curr_index = 0
    swap_index = 1

    # index, value of smallest value seen so far
    swap_info = [1, items[1]]

    while is_sorted(items) == False or curr_index < len(items)-1:

        # Find smallest value from the current index onwards
        while swap_index < len(items)-1:

            # found smaller value than current value (potential swap)
            if items[curr_index] > items[swap_index]:
                # Smaller value is the smallest value seen so far
                if items[swap_index] < swap_info[1]:
                    # Assigned smallest value so far to current value at swap_index
                    swap_info[0] = swap_index
                    swap_info[1] = items[swap_index]

            swap_index += 1

        # NOTE: Should not swap if no smaller value found
        # swap value at curr_index with value at swap_index
        temp = items[swap_info[0]]
        items[swap_info[0]] = items[curr_index]
        items[curr_index] = temp
        curr_index += 1
        # reset swap_index to curr_index + 1 and swap value to list value at curr_index+1
        swap_info[0] = curr_index+1
        swap_info[1] = items[curr_index+1]


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
    pass


if __name__ == "__main__":
    # items = [1,3,2,1]
    # items = [1,2,3,4]
    items = [1, 2, 3, 1, 2, 5]
    print(is_sorted(items))
    selection_sort(items)
    print(items)
