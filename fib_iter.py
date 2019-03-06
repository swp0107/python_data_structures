def getFib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    first = 0
    second = 1
    next_value = first + second;
    for x in range(2,position):
        first = second
        second = next_value
        next_value = first + second
    return next_value

#test
print(getFib(0)) #should print 0
print(getFib(1)) #should print 1
print(getFib(2)) #should print 1
print(getFib(3)) #should print 2
print(getFib(4)) #should print 3
print(getFib(5)) #should print 5
print(getFib(6)) #should print 8
print(getFib(7)) #should print 13
print(getFib(8)) #should print 21
print(getFib(9)) #should print 34
