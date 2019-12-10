#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    min, max = min(numbers), max(numbers)

    # Create list of counts with a slot for each number in input range
    count_list = {}
    # Loop over given numbers and increment each number's count
    for num in range(min, max+1):
        if num in count_list:
            count_list[num] += 1
        else:
            count_list[num] = 1

    output_list = []

    # Loop over counts and append that many numbers into output list
    for key, value in count_list:
        while value > 0:
            output_list.append(key)

    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
