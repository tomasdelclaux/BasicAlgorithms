def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    maxValue = ints[0]
    minValue = ints[0]
    for value in ints:
        if value > maxValue:
            maxValue = value
        elif value < minValue:
            minValue = value
    return (minValue, maxValue)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((1,1)) == get_min_max([1,1,1,1,1]) else "Fail")
print ("Pass" if ((0,1)) == get_min_max([1,1,0,1,1]) else "Fail")
print ("Pass" if ((3,6)) == get_min_max([5,3,3,5,6,6,4,4,3,4,4]) else "Fail")

