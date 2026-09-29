class Solution:
    def pairSum(self, head):
        # Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Calculate maximum twin sum
        first = head
        second = prev
        max_sum = 0

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum