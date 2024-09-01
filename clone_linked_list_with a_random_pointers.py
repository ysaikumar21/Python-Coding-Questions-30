class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def clone_linked_list(head):
    if not head:
        return None

    # Step 1: Create a new linked list with copied nodes
    node_map = {}
    new_head = Node(head.data)
    node_map[head] = new_head
    curr = head.next
    new_curr = new_head
    while curr:
        new_node = Node(curr.data)
        node_map[curr] = new_node
        new_curr.next = new_node
        new_curr = new_curr.next
        curr = curr.next

    # Step 2: Handle random pointers
    curr = head
    new_curr = new_head
    while curr:
        new_curr.random = node_map[curr.random]
        curr = curr.next
        new_curr = new_curr.next

    return new_head

# Example usage
# Create a sample linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.random = head.next.next
head.next.random = head.next.next.next
head.next.next.random = head
head.next.next.next.random = head

# Clone the linked list
new_head = clone_linked_list(head)

# Print the original and cloned linked lists
def print_linked_list(head):
    curr = head
    while curr:
        print(f"Data: {curr.data}, Next: {curr.next}, Random: {curr.random}")
        curr = curr.next

print("Original Linked List:")
print_linked_list(head)

print("\nCloned Linked List:")
print_linked_list(new_head)