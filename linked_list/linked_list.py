# Class for representing a node in a linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Create a linked list from a list of integers   
def create(arr) -> Node:
    if arr is None or len(arr) == 0:
        return None
    
    curr = Node(arr[0])
    head = curr
    for i in range(1,len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next

    return head

# return a string representation of the linked list for convenience of printing
def to_string(node):
    s = []
    while node is not None:
        s.append(str(node.data))
        s.append("--")
        node = node.next
    s.pop()
    return "".join(s)
