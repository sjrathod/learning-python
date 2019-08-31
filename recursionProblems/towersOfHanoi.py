#!/usr/bin/python

def towersOfHanoi(n, fromTower, toTower, auxTower):
   print "Recursing for n="+str(n)+" fromTower="+fromTower+" toTower="+toTower
   if (n==1):
      print "Base CASE: Move disk 1 from tower="+fromTower+" to tower="+toTower
      return
   
   # Move (n-1) disks from A to B using C as aux
   towersOfHanoi(n=n-1, fromTower=fromTower, toTower=auxTower, auxTower=toTower)

   # Move remaining disks from A to C
   print "Move disk="+str(n)+" from tower="+fromTower+" to tower="+toTower

   #Move (n-1) disks from B to C using A as aux
   towersOfHanoi(n=n-1, fromTower=auxTower, toTower=toTower, auxTower=fromTower)


if __name__ == "__main__":
   
   # A is source
   # C is destination
   # B is aux
   towersOfHanoi(n=5, fromTower="A", toTower="C", auxTower="B")
