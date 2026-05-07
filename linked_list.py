class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False


ll = LinkedList()

ll.append(5)
ll.append(15)
ll.append(25)

print("Linked List:")
ll.display()

print("Search 15:", ll.search(15))
print("Search 100:", ll.search(100))