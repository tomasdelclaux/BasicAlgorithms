def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sortedInput = mergesort(input_list)

    output = [0,0]
    dimension1 = len(input_list) // 2
    dimension2 = len(input_list) - dimension1
    while len(sortedInput) > 0:
        if dimension2 >= dimension1:
            output[0] += sortedInput[-1]*(10**(dimension2-1))
            dimension2 -= 1
        else:
            output[1] += sortedInput[-1]*(10**(dimension1-1))
            dimension1 -= 1
        sortedInput.pop(-1)
    return output

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 7, 8, 3, 3, 2,1,1,7,7,5,4], [977431, 875321]])