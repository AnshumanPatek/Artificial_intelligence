cap1=0
cap2=0
jug1=4
jug2=3
print("Starting state = (0,0)")
print("Capacities = (4,3)")
print("final state =(2,y)")
print ("Rule 1 : Fill the 4 gallon jug ")
print ("Rule 2: Fill the 3 gallon jug")
print ("Rule 3: Empty the 4 gallon jug")
print ("Rule 4 : Empty the 3 gallon jug ")
print ("Rule 5: Pour some water from 3 gallon jug to fill the 4 gallon jug")
print ("Rule 6: Pour some water from 4 gallon jug to 3 gallon jug")
print ("Rule 7: Pour all the water from 3 gallon jug to 4 gallon jug")
print ("Rule 8: Pour all the water from 4 gallon jug to 3 gallon jug")


while cap1!=2:
  r=int(input("Enter rule->"))
  if(r==1):
    print ("Rule 1 : Fill the 4 gallon jug ")
    cap1=jug1
  if(r==2):
    print ("Rule 2: Fill the 3 gallon jug")
    cap2=jug2
  if(r==3):
    print ("Rule 3: Empty the 4 gallon jug")
    cap1=0
  if(r==4):
    print ("Rule 4 : Empty the 3 gallon jug ")
    cap2=0;
  if(r==5):
    print ("Rule 5: Pour some water from 3 gallon jug to fill the 4 gallon jug")
    t=jug2-cap2
    y=jug2
    cap1-=t
  if(r==6):
    print ("Rule 6: Pour some water from 4 gallon jug to 3 gallon jug")
    t=jug1-cap1
    cap1=jug1
    cap1-=t
  if(r==7):
    print ("Rule 7: Pour all the water from 3 gallon jug to 4 gallon jug")
    cap2+=cap1
    cap1=0
  if(r==8):
    print ("Rule 8: Pour all the water from 4 gallon jug to 3 gallon jug")
    cap1+=cap2
    cap2=0
  print(cap1,cap2)
