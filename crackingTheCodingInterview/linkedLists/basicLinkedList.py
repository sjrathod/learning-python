# A simple Python program to introduce a linked list 
import pdb
# Node class 
class Node: 
   # Function to initialise the node object 
   def __init__(self, data): 
      self.data = data # Assign data 
      self.next = None # Initialize next as null 


   # Linked List class contains a Node object 
class LinkedList: 
   # Function to initialize head 
   def __init__(self): 
      self.head = None

   # This function prints contents of linked list 
   # starting from head
   def printList(self):
      temp = self.head
      if temp is None:
         print "Empty LinkedList!!"
      while (temp):
         if temp.next is None:
            print temp.data
         else:
            print temp.data,"-->",
         temp = temp.next

   def insertAtTail(self, new_data=None):
      end = Node(new_data)
      if self.head is None:
         self.head = end
         return
      temp = self.head
      while temp.next:
         temp = temp.next
      temp.next = end
   
   def insertAtHead(self, new_data=None):
      start = Node(new_data)
      start.next = self.head
      self.head = start

   def insertAtNth(self, new_data=None, n=0):
      if n==0:
         self.insertAtHead(new_data)
      else:
         previous = current = self.head
         new_node = Node(new_data)
         count = 0
         while (count < n):
            previous = current
            current = current.next
            if current is None:
               break
            count += 1

         previous.next = new_node
         new_node.next = current

   def deleteHead(self):
      self.head = self.head.next

   def deleteNth(self, n=0):
      if n==0:
         self.deleteHead()
      else:
         count = 1
         current  = self.head

         while count < n:
            if current.next is None:
               break
            current = current.next
            count += 1

         if current.next:
            current.next = current.next.next

   def generateLLofNnodes(self, n=1):
      if n < 1:
         return
      data = 10  #start number
      # pdb.set_trace()
      current = self.head = Node(data)
      while n > 1:
         data += 1
         current.next = Node(data)
         current = current.next
         n -= 1

   def lengthofLL(self):
      current = self.head
      count = 0
      while current:
         current = current.next
         count += 1
      return count
      
# Code execution starts here 
if __name__=='__main__': 

   # Start with the empty list 
   llist = LinkedList() 

   llist.head = Node(1) 
   second = Node(2) 
   third = Node(3) 

   ''' 
   Three nodes have been created. 
   We have references to these three blocks as head, 
   second and third 

   llist.head	 second			 third 
      |			 |				 | 
      |			 |				 | 
   +----+------+	 +----+------+	 +----+------+ 
   | 1 | None |	 | 2 | None |	 | 3 | None | 
   +----+------+	 +----+------+	 +----+------+ 
   '''

   llist.head.next = second; # Link first node with second 

   ''' 
   Now next of first Node refers to second. So they 
   both are linked. 

   llist.head	 second			 third 
      |			 |				 | 
      |			 |				 | 
   +----+------+	 +----+------+	 +----+------+ 
   | 1 | o-------->| 2 | null |	 | 3 | null | 
   +----+------+	 +----+------+	 +----+------+ 
   '''

   second.next = third; # Link second node with the third node 

   ''' 
   Now next of second Node refers to third. So all three 
   nodes are linked. 

   llist.head	 second			 third 
      |			 |				 | 
      |			 |				 | 
   +----+------+	 +----+------+	 +----+------+ 
   | 1 | o-------->| 2 | o-------->| 3 | null | 
   +----+------+	 +----+------+	 +----+------+ 
   '''

   llist.printList()

