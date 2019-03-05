"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    length = len(input_array)
    index = int(length/2)
    length = length/2
    while (1):
        if value == input_array[index]:
            return (index)
        if length == 0:
            return -1
        elif value > input_array[index]:
            if length % 2 == 0:
                length = length/2
                index = index + length
            else:
                length = int(length/2)
                index = index + length + 1
        elif value < input_array[index]:
            if length % 2 == 0:
                length = length/2
                index = index - length - 1
            else:
                length = int(length/2)
                index = index - length - 1
    return -1

test_list = [0,1,3,9,11,15,19,29]
test_val1 = 1
test_val2 = 3
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
test_val1 = 9
test_val2 = 11
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
test_val1 = 15
test_val2 = 19
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
test_val1 = 29
test_val2 = 25
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
test_val1 = 0
test_val2 = 5
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
test_val1 = 7
test_val2 = 8
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
