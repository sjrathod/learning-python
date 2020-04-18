#!/usr/bin/python

from collections import deque
import pdb

class Stack(deque):
   # function to initialize the deque
   def __init__(self, iterable=(), maxLength=None):
      super(Stack, self).__init__(iterable, maxLength)
   
   def peek(self):
      print "Sagar printing self=", self
      if self:
         return self[-1]
      else:
         return "Empty Deque"

def myStack():

   s = deque()
   print s

   s.extend("123")
   print s[-1]

def main():
   s = deque("efg")
   print s
   print list(s)
   for each in s:
      print each

   print "Appending and Extending"

   s.append("h")
   print list(s)
   s.extend("ij")
   print list(s)

   s.appendleft("d")
   print list(s)
   s.extendleft("abc")
   print list(s)

   print "Popping"
   s.pop()
   print list(s)
   s.popleft()
   s.popleft()
   s.popleft()
   print list(s)

   print "Reverse"
   print list(reversed(s))
   s.reverse()
   print list(s)
   s.reverse()
   print list(s), "back to unreversed"
   print "Rotate"
   s.rotate(1)
   print list(s), "<--rotated right"
   s.rotate(-2)
   print list(s), "<--rotated left"

if __name__ == "__main__":
   # main()
   myStack()