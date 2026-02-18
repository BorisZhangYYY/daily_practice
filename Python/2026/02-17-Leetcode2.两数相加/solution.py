from typing import Optional

"""
Definition for singly-linked list. In Leetcode, this class is defined, so when commit to Leetcode,
we need to delete the class ListNode.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        if val >= 0 and val < 10 and val is not None:
            self.val = val
        else:
            raise ValueError('val must be between 0 and 9')
        self.next = next
    def __repr__(self):
        return f'{self.val} -> {self.next}'
    def __len__(self):
        return 1 + len(self.next) if self.next else 1

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        max_len = max(len(l1_list), len(l2_list)) # 取较长的链表长度
        l1_list += [0] * (max_len - len(l1_list)) # 预构造
        l2_list += [0] * (max_len - len(l2_list)) # 预构造

        l3_list = []
        carry = 0
        for i in range(max_len):
            total = l1_list[i] + l2_list[i] + carry
            if total >= 10:
                total -= 10
                carry = 1
            else:
                carry = 0
            l3_list.append(total)
        if carry:
            l3_list.append(1)

        head = ListNode(l3_list[0])
        cur = head
        for d in l3_list[1:]:
            cur.next = ListNode(d)
            cur = cur.next
        return head

def list_to_nodes(values):
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def nodes_to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out
                       
if __name__ == '__main__':
    s = Solution()
    l1 = list_to_nodes([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_nodes([9, 9, 9, 9])
    result = s.addTwoNumbers(l1, l2)
    print(nodes_to_list(result))

    l1 = list_to_nodes([2, 4, 3])
    l2 = list_to_nodes([5, 6, 4])
    result = s.addTwoNumbers(l1, l2)
    print(nodes_to_list(result))
    




