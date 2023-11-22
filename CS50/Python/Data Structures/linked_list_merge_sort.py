
from LinkedList import Linked_list


def merge_sort(Linked_list):
    """
    Sorts a linked list in ascending order
        -Recursively divide the linked list into sublists containing a single node
        -Repeatedly merge the sublists to produce sorted sublists until one remains
        Returns a sorted linked list
    """
    if Linked_list.size() == 1:
        return Linked_list
    elif Linked_list.head is None:
        return Linked_list

    left_half, right_half = split(Linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(Linked_list):
    """
    Divide the unsorted linked list at midpoint into sublists
    """
    if Linked_list == None or Linked_list.head == None:
        left_half = Linked_list
        right_half = None

        return left_half, right_half
    else:
        size = Linked_list.size()
        mid = size//2

        mid_node = Linked_list.node_at_index(mid-1)
        left_half = Linked_list
        right_half = Linked_list()
        right_half = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Merges two linked list, sorting by data in nodes
    Returns a new merged list
    """
    # Create a mew linked list that contains nodes from merging left and right

    merged = Linked_list()

    # Add a fake head that is discarded later
    current = merged.head

    # Obtain head nodes for left and right linked list
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either

    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to false
            right_head = right_head.next_node
        # if the head node of right is None, we're past the tail
        # Add the node from left to merged linked
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right,set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node

    # Move current to next_node
    current = current.next_node

    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged


l = Linked_list()
l.add(3)
l.add(5)
l.add(0)
l.add(1)
l.add(2)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
