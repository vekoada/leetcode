

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = nodes.pop(0)
            self.head = node
        for ele in nodes:
            node.next = ListNode(val=ele)
            node = node.next
    
    def __iter__(self):
        node = self.head
        if node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        current = self.head
        while current.next is not None:
            current = self.next
        current.next = node
        node.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = LinkedList()
        for v1 in list1:
            for v2 in list2:
                if v1.val == v2.val:
                    if merge.head is None:
                        merge.add_first(v2)
                        merge.add_first(v1)
                    else:
                        merge.add_last(v1)
                        merge.add_last(v2)
                elif v1.val > v2.val:
                        if merge.head is None:
                            merge.add_first(v2)
                        else:
                            merge.add_last(v2)
                else: 
                    if merge.head is None:
                        merge.add_first(v1)
                    else:
                        merge.add_last(v1)
        return merge.head


#Iterate through both
# if element of one is equal to element of the other, add one and then the other 
# if element is greater than other, add smaller element and increment