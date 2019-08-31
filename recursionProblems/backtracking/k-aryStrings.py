#!/usr/bin/python
import sys
import pdb

myStr = list()
def k_aryStrings(n, k):
   global myStr
   # print "Entered k_aryStrings for n=%d and k=%d",n,k
   if n < 1:
      print "myStr="+"".join(myStr)
      return
   
   else:
      # pdb.set_trace()
      # loop to make 'k' branches in recursion
      # because a position can be filled with 'k' ways
      for i in range(0,k):
         myStr[n-1] = str(i)
         k_aryStrings(n-1, k)


   return

def main(argv):
   global myStr
   print 'Number of arguments:', len(argv), 'arguments.'
   print 'Argument List:', str(argv)
   lenOfStr = int(argv[0])
   k = int(argv[1])
   myStr = range(lenOfStr)
   k_aryStrings(n = lenOfStr, k = k)



if __name__ == "__main__":
   main(sys.argv[1:])


