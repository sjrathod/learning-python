
from collections import deque
import pdb
import sys

class MaxStack(list):
   def push(self, x):
      m = max(x, self[-1][1] if self else None)
      self.append((x, m))

   def pop(self):
      return list.pop(self)[0]

   def top(self):
      return self[-1][0]

   def peekMax(self):
      return self[-1][1]

   def popMax(self):
      m = self[-1][1]
      b = []
      while self[-1][0] != m:
         b.append(self.pop())

      self.pop()
      map(self.push, reversed(b))
      return m

   def userAppend(self):
      data = int(raw_input("User Append value="))
      self.push(data)

   def printMax(self):
      print "MAX=", self.peekMax()   


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


def main(inpArgs):

   print inpArgs
   s = MaxStack()
   print s
   pdb.set_trace()

   s.userAppend()
   s.printMax()
   s.userAppend()
   s.printMax()
   s.userAppend()
   s.printMax()
   s.userAppend()
   s.printMax()
   s.userAppend()
   s.printMax()

   pdb.set_trace()
   s.pop()
   s.printMax()
   s.popMax()
   s.printMax()
   s.pop()
   s.printMax()
   s.pop()
   s.printMax()
   s.popMax()
   s.printMax()


if __name__ =="__main__":
   main(sys.argv[1:])