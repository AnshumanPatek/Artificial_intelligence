print("Missionaries and Cannibals Problem");
print("Rule 1 : One Missionary is selling boat from bank 1 to Bank2");
print("Rule 2 : Two Missionary are selling boat from Bank 1 to Bank2");
print("Rule 3 : One Missionary is and One Cannibal are selling boat from bank 1 to Bank2");
print("Rule 4 : One Cannibal is selling boat from bank 1 to Bank2");
print("Rule 5 : Two Cannibal are selling boat from bank 1 to Bank2");
print("Rule 6 : One Missionary is selling boat from bank 2 to Bank1");
print("Rule 7 : Two Missionary are selling boat from bank 2 to Bank1");
print("Rule 8 : One Missionary and One cannibal are selling boat from bank 2 to Bank1");
print("Rule 9 : One Cannibal is selling boat from bank 2 to Bank1");
print("Rule 10 : Two Cannibals is selling boat from bank 2 to Bank1");

M1=3
C1=3
M2=0
C2=0
print("Start state = (3M,3C,Bank-1)")
print("final state = (3M,3C,Bank-2)")
while ((M2 != 3) or (C2!=3)):
 r = int(input("Enter rule--> "))
 if(r == 1): #(1M,0C) Rule 1
  M1-=1
  M2+=1

 elif(r == 2): #(2M,0C) Rule 2
  M1-=2
  M2+=2
 elif(r == 3):#(1M,1C) Rule 3
  M1-=1
  C1-=1
  M2+=1
  C2+=1
 elif(r == 4):#(0M,1C) Rule 4
  C1-=1
  C2+=1
 elif(r == 5):#(0M,2C) Rule 5
  C1-=2
  C2+=2
 elif(r == 6):#(1M,0C) Rule 6
  M1+=1
  M2-=1
 elif(r == 7):#(2M,0C) Rule 7
  M1+=2
  M2-=2
 elif(r == 8):#(1M,1C) Rule 8
  M1+=1
  C1+=1
  M2-=1
  C2-=1
 elif(r==9):#(0M,1C) Rule 9
  C1+=1
  C2-=1
 elif(r==10):#(0M,2C) Rule 10
  C1+=2
  C2-=2
 print (M1, C1)
 print (M2, C2)
 if((M1>0 and M1<C1) or (M2>0 and M2<C2)):
    print("dead")
    break




print("Missionaries and Cannibals Problem");
print("Rule 1 : One Missionary is selling boat from bank 1 to Bank2");
print("Rule 2 : Two Missionary are selling boat from Bank 1 to Bank2");
print("Rule 3 : One Missionary is and One Cannibal are selling boat from bank 1 to Bank2");
print("Rule 4 : One Cannibal is selling boat from bank 1 to Bank2");
print("Rule 5 : Two Cannibal are selling boat from bank 1 to Bank2");
print("Rule 6 : One Missionary is selling boat from bank 2 to Bank1");
print("Rule 7 : Two Missionary are selling boat from bank 2 to Bank1");
print("Rule 8 : One Missionary and One cannibal are selling boat from bank 2 to Bank1");
print("Rule 9 : One Cannibal is selling boat from bank 2 to Bank1");
print("Rule 10 : Two Cannibals is selling boat from bank 2 to Bank1");

M1=3
C1=3
M2=0
C2=0
print("Start state = (3M,3C,Bank-1)")
print("final state = (3M,3C,Bank-2)")
while ((M2 != 3) or (C2!=3)):
 r = int(input("Enter rule--> "))
 if(r == 1): #(1M,0C) Rule 1
  M1-=1
  M2+=1

 elif(r == 2): #(2M,0C) Rule 2
  M1-=2
  M2+=2
 elif(r == 3):#(1M,1C) Rule 3
  M1-=1
  C1-=1
  M2+=1
  C2+=1
 elif(r == 4):#(0M,1C) Rule 4
  C1-=1
  C2+=1
 elif(r == 5):#(0M,2C) Rule 5
  C1-=2
  C2+=2
 elif(r == 6):#(1M,0C) Rule 6
  M1+=1
  M2-=1
 elif(r == 7):#(2M,0C) Rule 7
  M1+=2
  M2-=2
 elif(r == 8):#(1M,1C) Rule 8
  M1+=1
  C1+=1
  M2-=1
  C2-=1
 elif(r==9):#(0M,1C) Rule 9
  C1+=1
  C2-=1
 elif(r==10):#(0M,2C) Rule 10
  C1+=2
  C2-=2
 print (M1, C1)
 print (M2, C2)
 if((M1>0 and M1<C1) or (M2>0 and M2<C2)):
    print("dead")
    break




