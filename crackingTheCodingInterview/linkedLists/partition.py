#! /usr/bin/python
from basicLinkedList import *
import pdb

def partition(current, k):
   
   beforeLL = LinkedList()
   afterLL = LinkedList()

   while current:
      if current.data < k :
         beforeLL.insertAtTail(current.data)
      else:
         afterLL.insertAtTail(current.data)
      current = current.next

   print "Before partition LL"
   beforeLL.printList()
   print "After partition LL"
   afterLL.printList()
   temp = beforeLL.head
   while temp.next:
      temp = temp.next
   
   temp.next = afterLL.head

   return beforeLL

def main():
   llist = LinkedList()
   llist.generateLLofNnodes(n=5)
   llist.insertAtNth(11, 5)
   llist.insertAtNth(14, 2)
   llist.insertAtNth(10, 3)
   llist.insertAtNth(1, 6)
   llist.insertAtNth(20, 1)
   llist.printList()

   k = int(raw_input("Enter number for partition, K:"))

   resLL = partition(llist.head, k)

   print "Final LL"
   resLL.printList()
if __name__ == "__main__":
   main()