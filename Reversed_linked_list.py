class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
def Reverse_linked_list(head):
    prev=None
    curr=head
    next_node=None
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
reversed_head=Reverse_linked_list(head)
current=reversed_head
while current:
    print(current.data,end=" ")
    current=current.next
