#!/usr/bin/python

from collections import deque
import pdb

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
   main()