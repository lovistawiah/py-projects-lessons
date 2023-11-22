
from re import L


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublists created in previous step 
    Combines: Merge the sorted sublists created in previous step

Takes overall O(n log n) time
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists 
    Returns two sublists -left and right
    Takes O(log n) time
    """
    #FIXME: use recursive binary search to sort the list
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists(arrays),sorting them in the process 
    Returns a new merged list
    Takes overall O(n) time
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sort(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sort(list[1:])


alist = [23, 1, 5, 85, 8, 0, 7, 3]
l = merge_sort(alist)
print(verify_sort(alist))
print(verify_sort(l))
