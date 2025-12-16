import random, inquirer, time
choice_=[inquirer.List("option",message="your choice",choices=["scissors","stone","paper"])]
comp_choice=["scissors","stone","paper"]
player_wins=0
comp_wins=0
for i in range(3):
    comp=random.choice(comp_choice)
    #print(comp)
    # player= input("your choice(scissors,stone,paper)-")
    player=inquirer.prompt(choice_)
    player= player["option"]
    print(player)
    if player==comp:
        print(comp,"=",player,"game is draw")
    else:
        if (player=="scissors" and comp=="stone") or (player=="stone" and comp=="paper") or(player=="paper" and comp=="scissors"):
            print(comp,">",player,"comp wins")
            comp_wins+=1
        else:
            print(comp,"<",player,"player wins")
            player_wins+=1
        time.sleep(2)
        print()
if player_wins==comp_wins:
    print(comp_wins,"=",player_wins,"game is draw")
elif player_wins<comp_wins:
    print("computer wins the match by",comp_wins-player_wins )
else:
    print("player wins the match by",player_wins-comp_wins )


