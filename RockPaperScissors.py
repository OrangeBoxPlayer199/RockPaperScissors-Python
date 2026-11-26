import random
choices = ["rock","paper","scissors"]
print("rock beats scissors, paper beats rock, scissors beats paper ")
player = input("choose: rock, paper, scissors, quit ")
while player != "quit": 
    player = player.lower()
    computer = random.choice(choices)
    print ("you chose: " +player+ " and the computer chose: " +computer+ ".")
    if player == computer:
        print ("tie!")
    elif player == "rock":
        if computer == "scissors":
            print("win for you")
        else:
            print("win for computer")
    elif player == "scissors":
        if computer == "paper":
            print ("win for you!")
        else:
            print ("win for computer!")
    elif player == "paper":
        if computer == "rock":
            print (" win for you!")
        else:
            print ("win for computer!")
    else:
        print ("error") 
    print()
       player = input("choose rock, paper, scissors, quit") 