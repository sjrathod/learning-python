#! /usr/bin/python
from basicLinkedList import *
import pdb

def recursiveRev(prev, cur, newList):
   # pdb.set_trace()
   if cur == None:
      # pdb.set_trace()
      return
   elif cur.next == None :
      # pdb.set_trace()
      newList.head = cur

   temp = cur.next
   cur.next = prev
   prev = cur
   cur = temp

   recursiveRev(prev, cur, newList)

def iterativeRev(prev, cur, newList):
   while(cur != None):
      temp_next = cur.next
      cur.next = prev
      prev = cur
      cur = temp_next
   
   newList.head = prev
   return newList

def reverseLL(head):
   prev = None
   cur = head
   newList = LinkedList() 

   # recursiveRev(prev, cur, newList)
   iterativeRev(prev, cur, newList)
   return newList

def main():
   llist = LinkedList()
   llist.generateLLofNnodes(n=1)
   llist.printList()

   newList = reverseLL(llist.head)

   newList.printList()

if __name__ == "__main__":
   main()