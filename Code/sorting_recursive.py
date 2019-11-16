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
     Running time: O(N^2) running time
        Memory usage: O(N), because we are creating a new list when we merge the two sublists
        that are equal size to N (M+M = N)
    """
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
    """
        Running time: O(n+m) where n and m are lengths of two sorted lists
        Memory usage: O(n+m) where n and m are lengths of two sorted lists,
        Runnning and memory time is the same for all cases, because we always copy
        all elements from both lists to new merged list.
    """

    if len(items) == 1:
        return

    mid_point = len(items)//2
    left_array = items[0:mid_point]
    right_array = items[mid_point:]

    merge_sort(left_array)
    merge_sort(right_array)



    return merge(items_1, items_2)

    # split list(s) into two seperate lists
    # merge



    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order



def partition(arr,low,high):

    # track index of smaller value
    i = low-1
    pivot = arr[high]

    for j in range(low , high):

        # If current value is smaller than or eqaul to pivot
        if arr[j] <= pivot:

            # increment index of smaller value
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1






    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.

    Best and average case running time: O(nlogn) when two halves of the list
    partitioned equally due to well picked pivot near the median of the list

    Worst case running time: O(n^2) When the pivot is picked far from the median resulting if __name__ == '__main__':
        bad splits
    TODO: O(1) because everything is done inplace """

    # When a sublist is just one element, then that sublist is already sorted

    if low is None and high is None:
        low = 0
        high = len(items)-1

    if low < high:
        # get the pivot index
        pivot_index = partition(items, low, high)
        # left half of the list to be sorted
        quick_sort(items, low, pivot_index - 1)
        # right half of the list to be sorted
        quick_sort(items, pivot_index + 1, high)



    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


if __name__ == "__main__":
    # list_1 = sorted([3,1,4,7,9])
    # list_2 = sorted([2,6,5,4,3,3,3])
    # l1 = [1,1,1,1]
    # l2 = [1,2,3]
    # print(merge(list_1, list_2))

    # list_1, list_2 = [3,1,4,7,9], [2,6,5,4]
    single_list = [3,1,4,7,9,2,6,5,4]
    # [3,1,4,7,9]
    # single_list = [6,7,9,1,3]
    # print(merge_sort(single_list))
    # print(single_list)

    # print(partition(single_list, 0, 5))
    # print(single_list)
    quick_sort(single_list,0,len(single_list)-1)
    print(single_list)
    # print(split_sort_merge(single_list))
    # print(merge(list_1,list_2))
    # print(merge(l1,l2))
