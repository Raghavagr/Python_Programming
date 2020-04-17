import random
wins=0
losses=0
draw=0
is_ends = False
prompt = "Choose Rock 'r' OR Paper 'p' OR Scissor 's' OR \nTo Quit Choose 'q'"
while True:
    user_choice = input(prompt)
    while user_choice not in ['r','p','s','q']:
        user_choice = input(prompt)
    if user_choice == 'q':
        break
    else:
        comp_choice = random.choice(['r','p','s'])
        if(comp_choice == 'r'):
            move="Rock"
        elif comp_choice == 'p':
            move ="Paper"
        else:
            move = "Scissor"
        print("Computer Choice:- "+move)

        if comp_choice == user_choice:
           print("Draws!")
           draw+=1
        elif(comp_choice == 'r' and user_choice == 'p') or (comp_choice == 'p' and user_choice == 's') or (comp_choice == 's' and user_choice == 'r'):
            print("You Win!..")
            wins+=1
        else:
           print("You Loss!..")
           losses+=1

print("You have total: \n"+str(wins)+" No. of wins And \n"+str(losses)+" No. of losses And \n"+str(draw)+" No. of draws")
     

