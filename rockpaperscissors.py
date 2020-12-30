import random

def check(uo,co):
    if(uo=="rock"):
        if(co=="paper"):
            return("computer")
        elif(co=="scissors"):
             return ("user")

    elif(uo=="paper"):
        if(co=="scissors"):
            return("computer")
        elif(co=="rock"):
             return ("user")

    elif(uo=="scissors"):
        if(co=="paper"):
            return("user")
        elif(co=="rock"):
             return ("computer")

options=['rock','paper','scissors']
count_round=0
player_score=0
computer_score=0

print("Welcome to rock-paper scissors!!!! Please enter Y to start Playing")
user_req=input()

while(user_req == "Y"):

    count_round+=1
    print(" Round : ",count_round)

    computer_option=options[random.randint(0,2)]

    print(" Enter your option  ")
    user_option=input().lower()

    if(user_option not in options):
        print("You have entered wrong option. The game will be terminated ")
        break;

    result=check(user_option, computer_option)

    if(result=="user"):
         player_score+=1
         print("Congratulations! you've won!! ")
    else:
         computer_score+=1
         print(" The computer won! try again! ")

    print(" Enter Y if you want to play again. Click any key to exit")
    user_req=input()

    if(user_req != "Y"):
        print("See you soon!")
        print("Total number of rounds played ", count_round)
        print("Your score = ",player_score)
        print("Computer score =",computer_score)
        
        break;

         
    
