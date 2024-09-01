class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.child = None
        self.val = val

def flatten(head):
    """Flattens a multilevel doubly linked list.

    Args:
        head: The head node of the multilevel doubly linked list.

    Returns:
        The head node of the flattened doubly linked list.
    """

    if not head:
        return head

    current = head
    while current:
        if current.child:
            child_head = flatten(current.child)
            # Connect the child list to the current node
            child_head.prev = current
            current.next.prev = child_head
            current.next = child_head
            current = child_head
        else:
            current = current.next

    return head
# Create a multilevel doubly linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.child = Node(5)
head.next.next.child.next = Node(6)
head.next.next.child.next.next = Node(7)
head.next.next.child.next.next.next = Node(8)

# Flatten the list
flattened_head = flatten(head)

# Print the flattened list
current = flattened_head
while current:
    print(current.val, end=' ')
    current = current.next