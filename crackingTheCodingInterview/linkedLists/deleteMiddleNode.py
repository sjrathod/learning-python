#! /usr/bin/python
from basicLinkedList import *
import pdb

def deleteMiddleNode(tempNode):
   tempNode.data = tempNode.next.data
   tempNext = tempNode.next
   tempNode.next = tempNext.next

def main():
   llist = LinkedList()
   llist.generateLLofNnodes(n=5)
   llist.printList()
   temp = llist.head
   k = int(raw_input("Enter number from delete node in the range of 2 to 4, K:"))

   if k < 2 or k >4:
      print "Input invalid. Please follow instruction."
      return
   while k!=1:
      temp = temp.next
      k -= 1

   deleteMiddleNode(temp)

   llist.printList()
if __name__ == "__main__":
   main()