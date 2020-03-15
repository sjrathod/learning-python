#! /usr/bin/python
from basicLinkedList import *
import pdb

def kthToLast(llist, k):
   runner = llist.head
   lagger = llist.head

   while (k != 1):
      if runner is None:
         # pdb.set_trace()
         return False
      runner = runner.next
      k -= 1

   
   while (runner.next != None):
      runner = runner.next
      lagger = lagger.next
   
   return lagger.data

def main():
   llist = LinkedList()
   llist.generateLLofNnodes(n=5)
   llist.printList()
   k = raw_input("Enter number from last node, K:")


   #returnKthToLast
   res = kthToLast(llist, int(k))
   if not res:
      print "K is out of range"
   else:
      print "Result: Kth element from last=", res

if __name__ == "__main__":
   main()
