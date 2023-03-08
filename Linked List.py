# Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Linked List Traversal 
    def display(self):
        item = self.head
        while item:
            print(item.data, end=" ")
            item = item.next
        print('\n')
    #Insert at the front of the linked list
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node


    #Insert node after a given node
    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node


    def append(self, new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node



    def traversal(self):
        if self.head is None:
            return "List is empty"
        pos = self.head
        while pos is not None:
            print(pos.value)
            pos = pos.next

    def search(self, value):
        if self.head is None:
            return "List is empty"
        else:
            node = self.head
            while node:
                if node.value == value:
                    print("It exists")
                    return
                node = node.next
            print("It doesn't exist")
            return


SLinkedList = SinglyLinkedList()


# SLinkedList.head = node1
# SLinkedList.head.next = node2
# SLinkedList.tail = node2
SLinkedList.append(1)
SLinkedList.append(2)
SLinkedList.append(3)
SLinkedList.append(4)
SLinkedList.append(5)
SLinkedList.append(6)
SLinkedList.search(8)
SLinkedList.traversal()