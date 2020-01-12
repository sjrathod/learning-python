#!/usr/bin/python

def checkPermutation2(str1, str2):
   # check if 2 string have exact character counts in the ASCII 128 range
   if (len(str1) != len(str2)):
      return False

   letters = {}
   for i in range(len(str1)):
      if ord(str1[i]) in letters.keys():
         letters[ord(str1[i])] = letters[ord(str1[i])] + 1
      else:
         letters[ord(str1[i])] = 1

   print "DEBUG: letters=", letters
   for i in range(len(str2)):
      if ord(str2[i]) in letters.keys():
         letters[ord(str2[i])] = letters[ord(str2[i])] - 1
      else:
         return False
      if letters[ord(str2[i])] < 0 :
         return False
   
   return True

def checkPermutation1(str1, str2):
   # there is a bug in the following logic
   # this fails when there are multiple entries of same letter for than one instance

   if (len(str1) != len(str2)):
      return False
   hashPerm = {}
   for i in range(len(str1)):
      hashPerm[str1[i]] = i
   
   print "DEBUG: hashPerm =", hashPerm

   for j in range(len(str2)):
      if str2[j] not in hashPerm.keys():
         return False

   return True

def main():

   str1 = raw_input("Enter string 1:")
   str2 = raw_input("Enter string 2:")

   # res = checkPermutation1(str1, str2)
   res = checkPermutation2(str1, str2)

   if (res):
      print "Strings are exact permutations of each other"
   else:
      print "Strings are NOT permutation of each other"

if __name__ == "__main__":
   main()