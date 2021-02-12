class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs1(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next
    return root.next


def swapPairs2(head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next

        head.next = swapPairs2(p.next)
        p.next = head
        return p
    return head