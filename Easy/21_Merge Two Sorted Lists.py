class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Dummy node to act as the start of the merged list
        dummy = ListNode()
        # Pointer to the current node in the new list
        current = dummy
        
        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Append the smaller value
                list1 = list1.next    # Move to the next node in list1
            else:
                current.next = list2  # Append the smaller or equal value
                list2 = list2.next    # Move to the next node in list2
            current = current.next    # Move to the next node in the merged list
        
        # Append the remaining nodes in list1 or list2 (only one will have remaining nodes)
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list starting from the first real node
        return dummy.next

def to_linked_list(items):
    dummy = ListNode(0)
    current = dummy
    for item in items:
        current.next = ListNode(item)
        current = current.next
    return dummy.next


def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# chk Test cases

list1 = to_linked_list([1, 2, 4])
list2 = to_linked_list([1, 3, 4])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print(to_list(merged_list))  


list1 = to_linked_list([])
list2 = to_linked_list([])
merged_list = solution.mergeTwoLists(list1, list2)
print(to_list(merged_list))

list1 = to_linked_list([])
list2 = to_linked_list([0])
merged_list = solution.mergeTwoLists(list1, list2)
print(to_list(merged_list)) 
