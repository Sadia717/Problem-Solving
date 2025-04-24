import time
import random
name1=input("Enter the player1 ")
name2= input("Enter the player2 ")
print("Computer has fixed 5 number integers in its mind")
print("You both have three turns each to guess it")
print("Ready for the game?")
nums=[]
while(len(nums)!=5):
    r=random.randint(1,10)
    if r not in nums:
        nums.append(r)
#print(nums)

player1=[]
player2=[]
s1=0
s2=0

for i in range(3):
    print("Hi {} Guess ur choice No {}".format(name1,i+1))
    x1=int(input())
    while(x1 in player1 or x1 in player2):
        print("Already choosen, so guess someother number")
        x1=int(input())
    player1.append(x1)
    if x1 in nums:
        print("-->CORRECT")
        s1=s1+1
    else:
        print("-->WRONG")

    print("Hi {} Guess ur choice No {}".format(name1,i+1))
    x2=int(input())
    while(x2 in player1 or x2 in player2):
        print("Already choosen, so guess someother number")
        x2=int(input())
    player2.append(x2)
    if x2 in nums:
        print("-->CORRECT")
        s2=s2+1
    else:
        print("-->WRONG")
print("------------")
print("Lets have summary")
print("Comp has chosen {}".format(nums))
print("{} has choosen {}".format(name1,player1))
print(f"(name1) score is (s1)")
print("{} has choosen {}".format(name2,player2))
print(f"(name2) score is (s2)")
if s1<s2:
    print("{} has won the game with score {}".format(name2,s2))
elif s1>s2:
    print("{} has won the game with score {}".format(name2,s2))
elif(s1==s2):
    print("-----DRAWN-----")
else:
    print("-----WRONG-----")