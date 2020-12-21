#-----------------------------------
#EE 381 fall 2020 Project 3- Part 1
#Name: Nhan Vo
#I.D.#017771388
#Start Date:
#End Date:
#Simulation of a discrete Markov chain
#------------------------------------
import random
step=[]#Record of particle locations

p_A=float(input("Enter the probability of going from '0' to '1'."))

p_B=float(input("Enter the probability of going from '1' to '0'."))

S=int(input("Enter either a '0' or a '1' for the starting position."))

step.append(S)#Put the starting location in the list.

#------------------------------------------------------------------------

for i in range(24):
    
    r=random.uniform(0,1)

    if r< p_A and S==0:#Particle at node 0 and RV A indeicates move.
        S=1
    elif r<p_B and S==1:#Particle at node 1 and RV B indeicates move.
        S=0
    step.append(S)
#------------------------------------------------------------------------

for i in step:
    print(i, end=" ")#printing the target variable which is the locations.
    
    
