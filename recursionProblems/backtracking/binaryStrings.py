#!/usr/bin/python
import sys
import pdb

myStr = list()
def binaryStrings(n):
   global myStr
   print "Entered binaryStrings for n=", n
   if n < 1:
      print "myStr="+"".join(myStr)
      return
   
   else:
      myStr[n-1] = '0'
      binaryStrings(n-1)
      myStr[n-1] = '1'
      binaryStrings(n-1)

   return

def main(argv):
   global myStr
   print 'Number of arguments:', len(argv), 'arguments.'
   print 'Argument List:', str(argv)
   lenOfStr = int(argv[0])
   myStr = range(lenOfStr)
   binaryStrings(n = lenOfStr)



if __name__ == "__main__":
   main(sys.argv[1:])


