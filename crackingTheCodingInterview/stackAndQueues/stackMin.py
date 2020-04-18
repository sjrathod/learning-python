#!/usr/bin/python

from collections import deque
import pdb
import sys
from stacks import Stack


class StackWithMin(Stack):

   def __init__(self):
      super(StackWithMin, self).__init__()
      self.sMin = []
   
   def min(self):
      if self.sMin:
         return self.sMin[-1]
      else:
         "Empty sMin"

   def printMin(self):
      min = self.min()
      # pdb.set_trace()
      print "Min in Stack is :", min
      # if min is int:
      #    print "Min in Stack is :", min
      # else:
      #    print min
   
   def userAppend(self):
      data = int(raw_input("User Append value="))
      self.append(data)
      if self.sMin:
         if self.min() > data:
            self.sMin.append(data)
      else:
         self.sMin.append(data)

   def userPop(self):
      value = self.pop()
      print "Popped", value
      if self.min() == value:
         self.sMin.pop()

def main(inpArgs):

   print inpArgs
   s = StackWithMin()
   print s
   pdb.set_trace()

   s.userAppend()
   s.printMin()
   s.userAppend()
   s.printMin()
   s.userAppend()
   s.printMin()
   s.userAppend()
   s.printMin()
   s.userAppend()
   s.printMin()

   pdb.set_trace()
   s.userPop()
   s.printMin()
   s.userPop()
   s.printMin()
   s.userPop()
   s.printMin()
   s.userPop()
   s.printMin()
   s.userPop()
   s.printMin()
   



   

   


if __name__ =="__main__":
   main(sys.argv[1:])