#!/usr/bin/python
from basicLinkedList import *

def removedupsWithoutUsingExtraMemory(llist):

   current = llist.head
   while current is not None:
      previous = current
      runner = current.next
      while runner is not None:
         if current.data == runner.data:
            previous.next = runner.next
            runner = runner.next
            continue
         runner = runner.next
         previous = previous.next
      
      current = current.next

def removedups(llist):

   data_set = set()
   previous = current = llist.head

   while current is not None:
      if current.data in data_set:      
         #remove this node
         previous.next = current.next
         current = current.next
         continue
      data_set.add(current.data)
      previous = current
      current = current.next
      print "Data set=", data_set

   return

def main():
   llist = LinkedList()
   llist.generateLLofNnodes(n=10)
   llist.printList()

   llist.insertAtNth(new_data=11, n=4)
   llist.insertAtNth(new_data=13, n=8)
   "After insertion"
   llist.printList()

   # removedups(llist)
   # llist.printList()

   removedupsWithoutUsingExtraMemory(llist)
   llist.printList()

if __name__ == "__main__":
   main()
