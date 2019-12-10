#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n*m) where n is the length of numbers and m is the unique values in numbers
    TODO: Memory usage: O(n) Copying to an output list"""

    # O(2n)
    maximum, minimum = max(numbers), min(numbers)

    # Find range of given numbers (minimum and maximum integer values)
    numbers_range = (maximum - minimum) + 1

    # Create list of counts with a slot for each number in input range
    count_list = [0]*numbers_range

    # Loop over given numbers and increment each number's count

    for num in numbers:
        count_list[num-minimum] += 1

    output_list = []

    # Loop over counts and append that many numbers into output list
    for num in count_list:
        while num > 0:
            output_list.append(num)
            num -= 1

    return output_list
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


if __name__ == "__main__":
    nums = [2,5,2,6,1,6,4,2,9]
    sorted_nums = counting_sort(nums)
    print(sorted(sorted_nums))
