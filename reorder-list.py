class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        O(N) time and O(1) space
        # Reaching the middle
        slow=head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reversing the second half
        prev = None
        current = slow
        nextNode = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head1 = prev
        current = ListNode()
        output = current
        # Merging the two
        while head.next:
            current.next = head
            head = head.next
            current = current.next
            current.next = head1
            head1 = head1.next
            current = current.next
        return output.next
        