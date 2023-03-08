#Linked list implementation

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

#Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

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


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

        
if __name__ == "__main__":
    
    lnk1 = LinkedList()

    #creating nodes
    lnk1.head = Node(1)
    lnk2 = Node(2)
    lnk3 = Node(3)

    #linking nodes
    lnk1.head.next = lnk2
    lnk2.next = lnk3

    lnk1.display()
    lnk1.push(5)
   


    # Insert 6.  So linked list becomes 6->None
    lnk1.append(6)
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    lnk1.push(7);
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    lnk1.push(1);
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    lnk1.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    lnk1.insertAfter(lnk1.head.next, 8)
    lnk1.display()