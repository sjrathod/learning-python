#!/usr/bin/python

def urlify(str1, tlen):
   wlen = len(str1)
   i = wlen - 1
   j = tlen - 1

   mystr = [char for char in str1]
   print "Before modification: ", mystr
   # import pdb;pdb.set_trace()
   # Using while loop here is important because we want to modidy
   # the iterator after inserting %20
   while i >= 0:
      if mystr[j] == " ":
         # pdb.set_trace()
         mystr[i - 1] = "0"
         mystr[i - 2] = "2"
         mystr[i - 3] = "%"
         i = i - 1
      else:
         mystr[i] = mystr[j]
      j = j - 1
      i = i - 1
   
   print "Final urlified string: ", mystr
   return "".join(mystr)

def main():
   # str1 = raw_input("Enter string with extra space:")
   # tlen = raw_input("Enter true length of the string")
   str1 = "Mr John Smith    "
   tlen = 13

   resultStr = urlify(str1, tlen)
   print "resultStr:", resultStr
   print "str1", str1


if __name__ == "__main__":
   main()