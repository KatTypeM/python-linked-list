# Python algorithm

# Linked list reverse

# from learning youtube https://www.geeksforgeeks.org/python-linked-list/
# annotated and changed by Kat Type M Productions

# class node with data and next
# things to add to linked list
    # constructor
    # insert beginning
    # insert at index
    # insert at end
    # remove first
    # remove from index    
    # remove last
    # update data
    # index of
    # is empty
    # Print ll
    # print size
    # reverse


# linked list node creation constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list control creation
class LinkedList:
    # Upon linked list initionation creation of head element
    def __init__(self):
        self.head = None
    
    # insert node at beginning
    def insertAtBegin(self, data):
        # create new node
        new_node = Node(data)
        # check if linked list is empty
        if self.head is None:
            self.head = new_node
            return
        else:
            # sets new node next element as what the current node pointer to head
            new_node.next = self.head
            # sets the self to head of linked list to the newly inserted node
            self.head = new_node
   
    # insert node at a particular index
    def insertAtIndex(self, data, index):
        # create new node
        new_node = Node(data)
        # start search at linked list head
        current_node = self.head
        # create position to compare to input parameter
        position = 0
        # compare index with position number for beginning of linked list
        if position == index:
            self.insertAtBegin(data)
        else:
        # start loop to compoare if position number and index number are the same. Looks ahead one index to set the position of the new node as the index 
            while(current_node != None and position+1 != index):
                # sets position to look at the next index number or the location of the place to insert the node before
                position = position+1
                # this sets the current node to the next in the sequence
                current_node = current_node.next
            # while loop stops when found the index and position are the same, then moves onto inserting node. The current node is the index before the inserted node.
            if current_node != None:
                # new node next is set to point to next node in the linked list 
                new_node.next = current_node.next
                # this sets the index before node to point to the new node
                current_node.next = new_node
            else:
                print("Index not present")
    
    # insert node at end of linked list
    def insertAtEnd(self, data):
        # create new node
        new_node = Node(data)
        # checks if linked list is empty
        if self.head is None:
            self.head = new_node
            return
        # sets current node at start of linked list
        current_node = self.head
        # if current node next is not null continue looping
        while(current_node.next):
            current_node = current_node.next
        # sets pointer of end node to point to new node
        current_node.next = new_node

    # function to update a nodes data
    def updateNode(self, val, index):
        # sets current node marker at beginning
        current_node = self.head
        # sets index counting position
        position = 0
        # check if editing the first node that is present
        if position == index:
            current_node.data = val
        else:
            # checks if the linked list is empty or the current node is the correct one as the index
            while(current_node != None and position != index):
                # iterates to the next node
                position = position + 1
                # sets the new node to look at
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else: 
                print("Index not present")
    
    
    def remove_first_node(self):
        # checks if the linked list is empty
        if(self.head == None):
            return
        # sets the head parameter to the next node data
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
        # loops and prints each nodes data
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    
    def sizeofLL(self):
        # sets the counter 
        size = 0
        if(self.head):
            current_node = self.head
            # loop through each node
            while(current_node):
                # adds one for each loop 
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0
            
    def reverseLL(self):
        # iniitalizes temp parameter
        prev = None
        # sets first node position
        current = self.head
        # checks if node next is pointing to another node
        while(current is not None):
        # two step process
        # step 1
            # store the next node pointer to into temp parameter
            next = current.next
            # set the current node to what the temp parameter, if at start of linked list sets the first node next to None. sets all others in second steop
            current.next = prev
        # step 2 (same as setting initial condition to start loop again)
            # sets the prev parameter from the initial settin to the current nods data
            prev = current
            # sets the next temp parameter that was from the pointer of the current next node
            current = next
        # sets the last node as the new head node
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
