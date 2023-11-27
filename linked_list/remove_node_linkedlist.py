import linked_list

def remove_last_nth_node(head, n):
    ptr1 = head
    ptr2 = head

    for i in range(n):
        if ptr2 is not None:
            ptr2 = ptr2.next
    
    prev = None
    while ptr2 is not None:
        prev = ptr1
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    if prev is not None:
        prev.next = ptr1.next
    else:
        head = ptr1.next

    return head

node = linked_list.create([3,5,2,6,8,7])
print(linked_list.to_string(node))

node = remove_last_nth_node(node, 2)
print(linked_list.to_string(node))




