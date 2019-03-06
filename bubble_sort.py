def bubble_sort(array):
    n = len(array)
    count = 1
    while (count):
        count = 0
        for x in range(0, n-1):
            if (array[x] > array[x+1]):
                tmp = array[x]
                array[x] = array[x+1]
                array[x+1] = tmp
                count += 1
        #this part is to show steps towards completed sort
        print (array)
    return array

#test
print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
