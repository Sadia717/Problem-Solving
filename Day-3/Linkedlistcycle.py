class Solution(object):
    def hasCycle(self, head):
        Fast = head
        Slow = head
        while(Fast is not None and Fast.next is not None):
            Fast = Fast.next.next
            Slow = Slow.next
            if(Fast == Slow):
                return True
        return False