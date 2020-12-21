#-----------------------------------
# EE 381 fall 2020 Project 3- Part 1
#Name: Nhan Vo
#I.D.#017771388
#Start Date:
#End Date:
#Simulation of a Bernoulli RV.
#------------------------------------

import random

p=float(input("Enter the probability of success"))# Bernoulli parameter
T= int(input("Enter the number of trials."))#How many runs?

for i in range(T):
    r=random.uniform(0,1)#random number
    if r<p:
        print("1",end=" ")#success

    else:
        print("0",end=" ")#failure

    
    
