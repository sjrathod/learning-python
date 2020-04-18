#!/usr/bin/python

from collections import deque
import pdb

class SetofStacks(list):

   def __init__(self, max_height):
      self.max_h = max_height
      self.curStack = 0

   def sosPush(self, data):
      if not self:
         self.append([])
      if len(self[self.curStack]) == self.max_h:
         self.append([])
         self.curStack += 1
      self[self.curStack].append(data)
   
   def sosPop(self):
      retPop = self[self.curStack].pop()
      if not self[self.curStack]:
         self.pop()
         self.curStack -= 1
      return retPop

   def popAt(self, index):
      return self.leftShift(index, True)

   def leftShift(self, index, removeTop):
      if index > len(self):
         return "Invalid index"
      stack = self[index]
      removedItem = None
      if removeTop:
         removedItem = stack.pop()
         print "RemovedFromTOP=", removedItem
      else:
         removedItem = self.removeBottom(index)
         print "RemovedFromBOTTOM=", removedItem

      if len(self) > index + 1:
         shiftedItem = self.leftShift(index+1, False)
         stack.append(shiftedItem)
         print "Appending Item=", shiftedItem
      elif self[index] == []:
         del self[index]

      return removedItem

   def removeBottom(self, index):
      stack = self[index]
      retItum = stack[0]
      del stack[0]
      return retItum

   def userAppend(self):
      data = int(raw_input("User Append value="))
      self.sosPush(data)


   def userPop(self):
      value = self.sosPop()
      print "Popped", value

  


def myStack():

   s = SetofStacks(2)
   pdb.set_trace()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   # s.userAppend()
   for i in range(0,11):
      s.sosPush(i)
   


   pdb.set_trace()
   s.userPop()

   s.popAt(2)

   s.userPop()


if __name__ == "__main__":
   # main()
   myStack()