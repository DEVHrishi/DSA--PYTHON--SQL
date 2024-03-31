'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.'''

'''approach:
1. using set
2. two pointer approach fast and slow (Tortoise and Hare Algorithm)
'''
# tc: O(n) and sc: O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store_node = set()
        head_node = head
        while head_node:
            if head_node in store_node:
                return True
            store_node.add(head_node)
            head_node = head_node.next
        return False
    
# tc: O(n) and sc: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False