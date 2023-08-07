# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1.next == None and l2.next != None):
            l1.next = ListNode(0)
        lout = ListNode((l1.val + l2.val)%10, l1.next)
        if(l1.val + l2.val > 9):
            if(l1.next != None):
                l1.next.val += 1
                # print(l1.next.val)
            else:
                l1.next = ListNode(1)
                lout.next = ListNode(1)

        while(l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next 
            l1.val += l2.val
            if(l1. val > 9): 
                if(l1.next == None):
                    l1.next = ListNode(1)
                    l1.val -= 10
                else:
                    l1.next.val += 1
                    l1.val -= 10
                    if(l1.next.val == 10 and l1.next.next == None):
                        l1.next.next = ListNode(1)
                        l1.next.val = 0
                    # elif(l1.next.val == 10):
                    #     l1.next.next.val += 1
                    #     l1.next.val = 0
            
            
        
        # print(l1)

        if(l1.next == None):
            print(l1, l2)
            l1.next = l2.next
        else:
            while(l1 != None):
                # print(l1.val, l1.next)
                if(l1.val >= 10):
                    if(l1.next == None):
                        l1.next = ListNode(1)
                        l1.val -= 10
                    else:
                        l1.next.val += 1
                
                l1.val = l1.val % 10
                l1 = l1.next

                if(l1 != None and l1.val < 10):
                    break 

        return lout
