# Python algorithm

# from learning youtube https://www.geeksforgeeks.org/python-linked-list/
# annotated and changed by Kat Type M Productions

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
   
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else: 
                print("Index not present")
    
    
    def remove_first_node(self):
        if(self.head == None):
            return
        self.head = self.head.next
        
    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
                
    def remove_node(self, data):
        current_node = self.head
        if current_node == data:
            self.remove_first_node()
            return
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
            
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    
    def sizeofLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0
            
    def reverseLL(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    
    
# to create a linked list create instance of class
llist = LinkedList()

# to add things to linked list
llist.insertAtEnd("a")
llist.insertAtEnd("b")
llist.insertAtBegin("c")
llist.insertAtEnd("d")
llist.insertAtIndex("g", 2)
llist.insertAtIndex("z", 4)

# test that data was inserted to the node properly
print("Node Data")
llist.printLL()

# test different type of remove functions
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)

print("\nLinked list after removing a node:")
llist.printLL()

# test if the update node function works
print("\nUpdate node Value")
llist.updateNode("zz", 0)
llist.printLL()

# prints out size of the linked list
print("\nSize of linked list: ", end=" ")
print(llist.sizeofLL())
    
# prints out the linked list in reverse
print("\nLinked list after it been reversed.")
llist.reverseLL()
llist.printLL()
