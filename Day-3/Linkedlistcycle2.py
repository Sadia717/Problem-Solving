class Solution(object):
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        Fast = head
        Slow = head
        while(Fast is not None and Fast.next is not None):
            Fast = Fast.next.next
            Slow = Slow.next
            if(Fast == Slow):
                break
        if(Fast is None or Fast.next is None):
            return None
        Slow = head
        while(Fast!=Slow):
            Slow = Slow.next
            Fast = Fast.next
        return Slow