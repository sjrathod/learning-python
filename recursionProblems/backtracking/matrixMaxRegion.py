#!/usr/bin/python
import sys
import pdb
import numpy as np 

maxsize = 0
size = 0
cntArr = []

def getVal(matrix, i, j, rmax, cmax):
   if (i<0) or (j<0) or i>rmax or j>cmax:
      return -1
   else:
      return matrix[i][j]

def findMaxRegion(matrix, r, c, rmax, cmax):
   global maxsize, size, cntArr
   if (r > rmax) or (c > cmax) or cntArr[r][c]==1:
      return
   print "Entering for r=%d and c=%d, maxsize=%d,size=%d", r, c, maxsize, size

   # cntarr[[]] tracks which blocks are traversed already no need to count it again.
   cntArr[r][c] = 1
   size += 1
   if size>maxsize:
      maxsize = size
      print "Maxsize=",maxsize
   found = 0
   # searh in all 8 directions for expanding the region by 1 block.
   # following are directional co-ordinate adjustments that needs 
   # to be made to look at 8 blocks around 1 block
   directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
   for dir in directions:
      newi = r + dir[0]
      newj = c + dir[1]
      val = getVal(matrix, newi, newj, rmax, cmax)
      if (val>0) and (cntArr[newi][newj]==0):
         print """newi={0},newj={1}""".format(newi, newj)
         found = 1
         findMaxRegion(matrix, newi, newj, rmax, cmax)
   if not found:
      size = 0

def getMaxOnes(matrix, rmax, cmax):

   for i in range(0, rmax):
      for j in range(0, cmax):
         if matrix[i][j]==1:
            findMaxRegion(matrix, i, j, rmax-1, cmax-1)

   print "Max Region size=",maxsize
   
def createMatrix(R, C):
   matrix = [] 
   print("Enter the entries rowwise:") 
   
   # For user input 
   for i in range(R):          # A for loop for row entries 
      a =[] 
      for j in range(C):      # A for loop for column entries 
            a.append(int(input())) 
      matrix.append(a)

   return matrix

def createFalseMatrix(R, C):
   global cntArr
   for i in range(R):          # A for loop for row entries 
      a =[] 
      for j in range(C):      # A for loop for column entries 
            a.append(0) 
      cntArr.append(a)

def main(argv):
   
   R = int(input("Enter the number of rows:")) 
   C = int(input("Enter the number of columns:")) 
   
   
   print("Enter the entries in a single line (separated by space): ") 
   
   # User input of entries in a  
   # single line separated by space 
   # pdb.set_trace()
   entries = list(map(int, raw_input().split()))
   matrix = np.array(entries).reshape(R, C) 
   print matrix

   # OR  Use followig rudimentary method to create matrix
   # Initialize matrix 
   # matrix = createMatrix(R, C)
   # print (matrix)

   createFalseMatrix(R, C)
   print cntArr
   getMaxOnes(matrix, R, C)

def test():
   mylist = raw_input("Enter the numbers:")
   print mylist
if __name__ == "__main__":
   # test()
   main(sys.argv[1:])