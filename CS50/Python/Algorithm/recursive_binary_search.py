def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                #list[midpoint+1:]: slice the array,starting after the midpoint to the end of the array
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                #list[midpoint+1:]: slice the array,starting at the beginning of the array to the midpoint 
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found", result)

#NOTE: Read tail optimization
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 4)
verify(result)
