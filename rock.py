import random
comp_wins=0
player_wins=0

def Choose_Opition():
    user_choice =input("Choose Rock, Paper , Scissors:")
    if  user_choice in ["Rock","rock","r","R"]:
         user_choice="r"
    elif user_choice in ["Paper","paper","p","P"]:
         user_choice="p"
    elif user_choice in["SCISSORS","scissors","S","s"]:
         user_choice="s"
    else:
        print(" I  don't understand  try again.")   
        Choose_Opition()
    return user_choice
def computer_choice():
    comp_choice = random.randint(1,3)
    if comp_choice== 1:
        comp_choice="r"
    elif comp_choice==2:
        comp_choice=="p"
    else:
        comp_choice="s"
    return comp_choice 
while True:
    print("")   
    user_choice =Choose_Opition()
    comp_choice=computer_choice()
    print("")
    if user_choice=="r":
       if comp_choice=="r":
         print("You choose rock.The computer chose rock.You tied. ")
    elif comp_choice=="p":
          print("You choose rock.The computer chose rock.You tied. ")
          comp_wins +=1
    elif comp_choice=="s":
          print("You choose rock.The computer chose rock.You tied. ")
          player_wins +=1

    elif user_choice=="p":  
        if comp_choice=="r":
            print("You choose rock.The computer chose rock.You tied. ")
            player_wins +=1 
    elif comp_choice=="p":
           print("You choose rock.The computer chose rock.You tied. ")
    elif comp_choice=="s":
            print("You choose rock.The computer chose rock.You tied. ")
            comp_choice+=1
    elif user_choice=="s":
         if comp_choice=="r":
             print("You choose rock.The computer chose rock.You tied. ")
             comp_choice+=1
         elif comp_choice  =="p": 
               print("You choose rock.The computer chose rock.You tied. ")
               player_wins+=1
         elif comp_choice=="s":   
              print("You choose rock.The computer chose rock.You tied. ")

              print("")
              print("Player wins:"+str(player_wins))
              print("Computer wins:"+str(comp_choice))
              print("")
         user_choice = input("Do you want to play  again?(Y/N)")
         if user_choice in ["Y","y","yes","YES"]:
                pass
         elif user_choice in ["N","n","no","NO"]:
                break
         else:
            break