#!python
from sorting_iterative import selection_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n+m) Have to iterate over each element in both lists. All conditions
    TODO: O(n+m) Append all values in both lists to a single list"""

    merged_list = []

    # longer list becomes primary list to add to in order to minimize number of iterations
    primary_list, secondary_list = (items1, items2) if len(items1) > len(items2) else (items2, items1)
    pl_index = 0
    sl_index = 0
    print(f"Primary List: {primary_list}")
    print(f"Secondary List: {secondary_list}")
    # while len(merged_list) != len(primary_list) + len(secondary_list):
    while sl_index < len(secondary_list) and pl_index < len(primary_list):
        print(merged_list)
        if primary_list[pl_index] < secondary_list[sl_index]:
            merged_list.append(primary_list[pl_index])
            pl_index += 1
        else:
            merged_list.append(secondary_list[sl_index])
            sl_index += 1


# + primary_list[pl_index:] + secondary_list[sl_index:]
    return merged_list + primary_list[pl_index:] + secondary_list[sl_index:]


    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    list1, list2 = items[0:len(items)//2], items[len(items)//2:]
    print(list1)
    print(list2)
    selection_sort(list1)
    selection_sort(list2)
    return merge(list1, list2)

    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # low index starts at 1 because pivot is init at index 0
    low_index, high_index = low+1, high-1
    pivot = items[low]

    # increment low_index until you find value greater than pivot
    # decrement high_index until you find value less than pivot
    # Swap the values at these indicies

    while low_index < high_index:

        # increment low_index until you find value greater than pivot
        while items[low_index] < pivot:
            # print("increment low_index until you find value greater than pivot")
            # print("low_index:", low_index)
            # print("high_index:", high_index)
            # print("increment")
            low_index += 1

        # decrement high_index until you find value less than pivot
        while items[high_index] > pivot:
            # print("decrement high_index until you find value less than pivot")
            # print("low_index:", low_index)
            # print("high_index:", high_index)
            # print("decrement")
            high_index -= 1

        # print("Swap!")
        # Swap values
        items[low_index], items[high_index] = items[high_index], items[low_index]
        low_index += 1
        high_index -= 1

    # print("Swap pivot with high_index")
    # Swap value at high index with pivot, indicating partioned array
    items[low], items[high_index] = items[high_index], pivot

    return high_index


    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


if __name__ == "__main__":
    # list_1 = sorted([3,1,4,7,9])
    # list_2 = sorted([2,6,5,4])
    # l1 = [1,1,1,1]
    # l2 = [1,2,3]

    # list_1, list_2 = [3,1,4,7,9], [2,6,5,4]
    # single_list = [3,1,4,7,9,2,6,5,4]
    # [3,1,4,7,9]
    single_list = [6,7,9,1,3]
    print(partition(single_list, 0, 5))
    print(single_list)
    # print(split_sort_merge(single_list))
    # print(merge(list_1,list_2))
    # print(merge(l1,l2))
