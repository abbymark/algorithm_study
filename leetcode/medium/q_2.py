from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    added_list = ListNode((l1.val+l2.val)%10)
    carry = (l1.val+l2.val)//10
    current_node = added_list

    while l1.next or l2.next:
        if l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val+l2.val+carry)//10
            current_node = current_node.next

        if l1.next and not l2.next:
            l1 = l1.next
            current_node.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val+carry)//10
            current_node = current_node.next

        if not l1.next and l2.next:
            l2 = l2.next
            current_node.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val+carry)//10
            current_node = current_node.next

        if carry:
            current_node.next = ListNode(carry)
    return added_list