#!/usr/bin/env python3
import random
from ex2_rpsls_helper import get_selection

#This function plays a rpsls game against the computer until 2.
def rpsls_game():
    
    plW,coW,dr=0,0,0
    rpsls=["Rock","Paper","Scissors","Lizard","Spock"]
    while abs(plW-coW)<2:
        plCh=(int)(input("    Please enter your selection: 1 (Rock), 2"+
              "(Paper), 3 (Scissors), 4 (Lizard) or 5 (Spock): "))
        if plCh>0 and plCh<6:
            plCh= plCh-1
            print("    Player has selected: %s." % rpsls[plCh])
            coCh=random.randint(0,4)
            print("    Computer has selected: %s." % rpsls[coCh])
            if plCh==coCh:
                print("    This round was drawn\n")
                dr=dr+1
            elif plCh==0:
                if coCh==3 or coCh==2:
                    plW=plW+1
                    print("    The winner for this round is: Player\n")
                else:
                    coW=coW+1
                    print("    The winner for this round is: Computer\n")
            elif plCh==1:
                if coCh==0 or coCh==4:
                    plW=plW+1
                    print("    The winner for this round is: Player\n")
                else:
                    coW=coW+1
                    print("    The winner for this round is: Computer\n")
            elif plCh==2:
                if coCh==1 or coCh==3:
                    plW=plW+1
                    print("    The winner for this round is: Player\n")
                else:
                    coW=coW+1
                    print("    The winner for this round is: Computer\n")
            elif plCh==3:
                if coCh==4 or coCh==1:
                    plW=plW+1
                    print("    The winner for this round is: Player\n")
                else:
                    coW=coW+1
                    print("    The winner for this round is: Computer\n")
            elif plCh==4:
                if coCh==2 or coCh==0:
                    plW=plW+1
                    print("    The winner for this round is: Player\n")
                else:
                    coW=coW+1
                    print("    The winner for this round is: Computer\n")
        else:
            print("    Please select one of the available options.\n")
    if coW-plW==2:
        print("The winner for this game is: Computer")
        print("Game score: Player %i, Computer %i, draws %i" % (plW, coW, dr))
        return -1
    print("The winner for this game is: Player")
    print("Game score: Player %i, Computer %i, draws %i" % (plW, coW, dr))
    return 1
    
    

def rpsls_play():
    #This function plays the game as many times as wanted.
    print("Welcome to the Rock-Scissors-Paper-Lizard-Spock game!")
    again=2
    stCnt=0
    stW=0
    while again!=1:
        stCnt= stCnt+1
        if again!=3:
            keep=(int)(input("Select set length: "))+1
        gmCnt=1
        plW=0
        coW=0

        #Plays the game if the player wishes to continue,
        #if we no player have the needed amount of wins,
        # or if the game is 
        while (((plW < keep//2 and coW < keep//2) and keep%2==0)
                or  (((plW <= keep//2 and coW <= keep//2) or abs(plW-coW)<2)
                           and keep%2==1)):
            print("Now beginning game %i" % gmCnt)
            gm=rpsls_game()
            if gm==1:
                plW = plW+1
            else:
                coW = coW+1
            gmCnt= gmCnt+1
            print("Set score: Player %i, Computer %i" % (plW,coW))
            
        gmCnt=gmCnt-1
        if plW>coW:
            print("Congratulations! You have won in %i games." % gmCnt)
            stW=stW+1
        else:
            print("Too bad! You have lost in %i games." %coW)
        print("You have played %i sets, and won %i!\n " % (stCnt,stW))
        again=(int)(input("Do you want to: 1 - quit, 2 - reset scores"+
                          " or 3 - continue? "))
        if again==2:
            print("Resetting scores")
                
    
##    rpsls_game() #somewhere you should use the above function
##    sel = random.randint(1,5) #Code for getting random numbers
##    get_selection(sel) #Get string, e.g., if sel==4, get_selection(sel)=="Lizard"

#Here to help you test your code.
#When debugging, it is helpful to be able to replay with the computer
# repeating the same choices.
if __name__=="__main__": #If we are the main script, and not imported
    from sys import argv
    try:
        random.seed(argv[1]) # as a string is good enough
    except:
        pass

    rpsls_play()
