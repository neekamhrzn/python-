import random

def winner(user,computer):
    if(user=='r' and computer=='s'):
        return True
    elif(user=='p' and computer=='r'):
        return True
    elif(user=='s' and computer=='p'):
        return True
    elif(user==computer):
        return None
    else:
        return False

computerPoints=0
playerPoints=0
ans='y'
choices=['r','p','s']

while(ans=='y'):
    user=input("Enter your choice:\nr for rock\np for paper\ns for scissors:\n")
    
    computer=random.randint(0,2)
    computer=choices[computer]

    win=winner(user,computer)

    print(f"\nYou chose {user} and computer chose {computer}")

    if(win==True):
        print("Congratulations, You Won! ")
        playerPoints+=1
    elif(win==False):
        print("Sorry, You lose! ")
        computerPoints+=1
    elif(win==None):
        print("Match Draw")
    else:
        print("Error! Please Try Again. ")
    
    ans=input("\nDo you want to play next round? (y/n): ")

print(f"Computer Points: {computerPoints}\nPlayer Points: {playerPoints}")
