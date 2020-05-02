def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def find_sorted(input_list, number):
        index = 0
        while len(input_list) >= 1:
            estimate = len(input_list)//2
            if input_list[estimate] == number:
                return estimate + index
            elif input_list[estimate] < number:
                index += len(input_list)//2+1
                input_list = input_list[len(input_list)//2+1:]
            elif input_list[estimate] > number:
                input_list = input_list[:len(input_list)//2]
        return -1

    index = 0
    while True:
        if len(input_list) <= 2:
            for i, value in enumerate(input_list):
                if value == number:
                    return index + i
                elif i == 1:
                    return -1
        leftHalf = input_list[:len(input_list)//2]
        rightHalf = input_list[len(input_list)//2:]
        if leftHalf[-1] > leftHalf[0]:
            if number >= leftHalf[0] and number <= leftHalf[-1]:
                found = find_sorted(leftHalf, number)
                if found != -1:
                    return found + index
                else:
                    return -1
            else:
                other = rightHalf
                index += len(input_list)//2
        else:
            if number >= rightHalf[0] and number <= rightHalf[-1]:
                found = find_sorted(rightHalf, number)
                if found != -1:
                    return found + index
                else:
                    return -1
            else:
                other = leftHalf
        input_list = other


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

