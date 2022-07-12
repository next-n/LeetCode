# https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next


def addTwoNumbers_Betterway(l1, l2):
    root = n = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        v = u = 0
        if l1:
            v = l1.val
            l1 = l1.next
        if l2:
            u = l2.val
            l2 = l2.next
        carry, val = divmod(v + u + carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next


def addTwoNumbers_naive(l1, l2):
    def helper(li):
        curval = [li.val]
        while li.next is not None:
            curval.insert(0, li.next.val)
            li = li.next
        alen = len(curval) - 1
        vlu = 0
        for x in curval:
            vlu += x * 10 ** alen
            alen -= 1
        return vlu

    value_of_l1 = helper(l1)
    value_of_l2 = helper(l2)
    value_add = value_of_l1 + value_of_l2
    ansarray = []
    while value_add > 0:
        ansarray.append(value_add % 10)
        value_add //= 10

    def helper2(arr):
        if len(arr) == 0: return ListNode(0)
        n1 = ListNode(arr[0])
        pointer = n1
        # if len(arr) == 0: return n1
        for x in range(1, len(arr)):
            nx = ListNode(arr[x])
            pointer.next = nx
            pointer = nx
        return n1

    return helper2(ansarray)

