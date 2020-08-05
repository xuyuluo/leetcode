class Solution:
    
    def list_to_number(l1: ListNote) -> int:
        
        factor = 1
        num = 0
        current = l1
        
        while current.next != None:
            num = num + current.val*factor
            factor = factor*10
            current = current.next
            
    def number_to_list(num: int) -> ListNote:
        
        factor = 10
        current = ListNode()
        while num/factor != 0:
            next_sl = num/factor
            nlist = ListNode(num - next_sl*factor)
            current.next
            num = next_sl
        print l
            
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
