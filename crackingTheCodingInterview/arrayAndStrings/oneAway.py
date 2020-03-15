#!/usr/bin/python

def oneAway(str1, str2):
   i = 0
   j = 0
   edited = False

   diff = len(str1) - len(str2)
   if diff < -1 or diff > 1:
      return False

   s1 = str1 if (len(str1) > len(str2)) else str2
   s2 = str2 if (len(str1) > len(str2)) else str1

   if diff == 0:
      while(i < len(s1) and j < len(s2)):
         if s1[i] != s2[j]:
            if edited:
               return False
            edited = True
            if diff == 0:
               j += 1
         else:
            j += 1
         
         i += 1
      
   return True

def main():
   str1 = raw_input("Enter string1 for one away check:")
   str2 = raw_input("Enter string2 for one away check:")

   if oneAway(str1, str2):
      print "Strings are one edit away."
   else:
      print "Strings are NOT one edit away."

if __name__ == "__main__":
   main()