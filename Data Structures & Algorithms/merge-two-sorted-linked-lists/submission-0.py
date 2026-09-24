# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        head1, head2 = list1, list2

        while head1 and head2: 
            if head1.val < head2.val: 
                tail.next = head1
                head1 = head1.next

            else: 
                tail.next = head2
                head2 = head2.next

            tail = tail.next
        if head1: 
            tail.next = head1
        elif head2: 
            tail.next = head2

        return dummy.next


# The time complexity is O(M+N), where M is the number of nodes in list1 and N is the number of nodes in list2.
# This is because the algorithm must look at every single node from both lists exactly once to decide its position in the final merged list. 
# The while loop iterates, and in each step, it advances one of the pointers (curr1 or curr2). 
# Since no node is ever visited more than once, the total number of operations is directly proportional to the total number of nodes.
