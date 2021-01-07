import random


def check(uo,co,dict_option):
    if(uo==option[0]):
        if(co==dict_options[option[0]][0]):
            return("computer")
        if(co==dict_options[option[0]][1]):
            return("user")
    if(uo==option[1]):
        if(co==dict_options[option[1]][0]):
            return("computer")
        if(co==dict_options[option[1]][1]):
            return("user")
    if(uo==option[2]):
        if(co==dict_options[option[2]][0]):
            return("computer")
        if(co==dict_options[option[2]][1]):
            return("user")

def printscore(count_round, player_score, computer_score):
        print("Total number of rounds played ", count_round)
        print("Your score = ",player_score)
        print("Computer score =",computer_score)
        print("See you soon!")



print("Pre-game setting procedure")
option=input("Enter options to play the game. Leave blank between the options. Please enter only 3 options").lower().split()
for i in option:
    print(i)

dict_options={}
dict_options[option[0]]=input("First enter losing option then winning option for ",option[0]).lower().split()
dict_options[option[1]]=input("First enter losing option then winning option for ",option[1]).lower().split()
dict_options[option[2]]=input("First enter losing option then winning option for ",option[2]).lower().split()


count_round=0
player_score=0
computer_score=0

print("Welcome to umrps!!!! Please enter Y to start Playing")
user_req=input()

while(user_req == "Y"):
    
    count_round+=1
    print("Round : ",count_round)

    computer_option=option[random.randint(0,2)]

    print("Enter your option  ")
    user_option=input().lower()
    
    wrong_input=0
    while(user_option not in option):
        print("You have entered wrong option. 3 more wrong entries and the game will be terminated")
        wrong_input+=1
        print("Number of wrong entries = ",wrong_input)
        user_option=input().lower()
        if(wrong_input>=2):
            print("Wrong option program terminated")
            printscore(count_round, player_score, computer_score)
            break

    if(wrong_input>=2):
        break

    result= check(user_option, computer_option, dict_options)
    

    if(result=="user"):
         player_score+=1
         print("Congratulations! you've won!! ")
    elif(result=="computer"):
         computer_score+=1
         print(" The computer won! try again! ")
    else:
        print("Draw!")
        player_score+=0.5
        computer_score+=0.5

    print(" Enter Y if you want to play again. Click any key to exit")
    user_req=input()

    if(user_req != "Y"):
        printscore(count_round, player_score, computer_score)
        break;

if(count_round<1):
  if(user_req != "Y"):
      printscore(count_round, player_score, computer_score)
