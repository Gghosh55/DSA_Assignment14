
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def newNode(data):
    new_node = Node(data)
    return new_node


def addCarry(head):
    if head is None:
        return 1

    res = head.data + addCarry(head.next)
    head.data = res % 10
    return res // 10


def add1One(head):
    carry = addCarry(head)

    if carry:
        new_node = newNode(carry)
        new_node.next = head
        return new_node

    return head


def printList(head):
    node = head
    while node is not None:
        print(node.data, end="")
        node = node.next
    print()


head = newNode(4)
head.next = newNode(5)
head.next.next = newNode(6)
head.next.next.next = newNode(6)
head.next.next.next.next = newNode(7)
head.next.next.next.next.next = newNode(8)

print("Linked list is: ", end="")
printList(head)

head = add1One(head)
print("After adding 1, new linked list is: ", end="")
printList(head)
