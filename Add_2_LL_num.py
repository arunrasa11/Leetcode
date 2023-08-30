# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


""" 
    Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    Output: [7, 0, 8]
    Explanation: 342 + 465 = 807.
    Example
    2:

    Input: l1 = [0], l2 = [0]
    Output: [0]
    Example
    3:

    Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    Output: [8, 9, 9, 9, 0, 0, 0, 1]
"""

class Solution:
    #def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    def addTwoNumbers(self, l1, l2):

        firstrObj = ListNode()
        carry = 0
        prev = None

        while l1 != None or l2 != None or carry !=0:

            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            carry, value = divmod((num1 + num2 + carry), 10)

            curNode = ListNode(value)
            if prev != None:
                prev.next = curNode
            else:
                firstrObj = curNode
            prev = curNode

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return firstrObj

            # if l1 != None and l2 != None:
            #     carry, value = divmod((l1.val + l2.val + carry), 10)
            #     l1 = l1.next
            #     l2 = l2.next
            # elif l1 != None:
            #     carry, value = divmod((l1.val + carry), 10)
            #     l1 = l1.next
            # elif l1 != None:
            #     carry, value = divmod((l1.val + l2.val + carry), 10)
            #     l2 = l2.next
            # else:
            #     carry, value = (0, carry)
            #
            # curNode = ListNode(value)
            # if prev != None:
            #     prev.next = curNode
            # else:
            #     firstrObj = curNode
            # prev = curNode






