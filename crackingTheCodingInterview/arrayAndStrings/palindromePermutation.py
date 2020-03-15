#! /usr/bin/python

import pdb
def generateCharFrequencyTable(testStr):
   table = {}
   for c in testStr:
      if c.isspace() is False:
         if c in table.keys():
            table[c] += 1
         else:
            table[c] = 1
   return table

def palinPerm(inpStr):
   testStr = inpStr.lower()

   charFrequencyTable = generateCharFrequencyTable(testStr)
   foundOdd = False
   # pdb.set_trace()
   for k in charFrequencyTable.keys():
      if charFrequencyTable[k]%2:
         if foundOdd:
            return False
         else:
            # Max one odd is allowed
            # When string is of even length then there will no odd characters
            # When string is of odd length then there will be exactly one char with odd instances
            foundOdd = True
   return True

def main():
   str1 = raw_input("Enter string for palindrome permutation check:")

   res = palinPerm(str1)
   if res:
      print "String is a palindrome permutation"
   else:
      print "String is NOT a palindrome permutation"

if __name__ == "__main__" :
   main()