# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        curr = dummy
        seen = set()
        
        while head is not None:
            if head.val not in seen:
                seen.add(head.val)
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next
                
        return dummy.next
    



# My idea is to have a dictionary/set to track the values in the node and a dummy node to attach the current value. If the value is not in the dictionary, we add it in to keep track and then add it to the dummy node. Else, if the frequency of a value in the dictionary  > 1: attach only 1 of the value to the dummy node, disregrading its duplicate