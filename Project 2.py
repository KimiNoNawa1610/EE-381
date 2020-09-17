#----------------
#EE 381 fall 2020
#Project 2
#Nhan Vo
#I.D. #017771388
#Start Date: 9-9-2020
#End Date:9-16-2020
#Simulation of a coin flip. Use simulation to determine probability of
#heads on an odd flip.
#----------------
import random# import random module

p= 0.5
game=[]#The results of one game
win =0#Accumulator for whether or not we won a game
N=100000#Number of experience

for i in range(N):
    Coin=0#Coin variable set to tails
    #-----------------------------------------------
    # Simulation
    #-----------------------------------------------
    while Coin!=1:# Run until coin comes up heads
        r=random.uniform(0,1)
        if r<p:
            Coin=0
        else:
            Coin=1
        game.append(Coin)# Record all flips for a single game.
    L=len(game)#The length of a run for an individual game.
    if L%2==1:#Was heads on an odd flip
        win+=1#If heads on odd flip increment wins

    game=[]#Reset
    #-----------------------------------------------

print("The probability of heads on an flip is: ",win/N,".")

        
   





