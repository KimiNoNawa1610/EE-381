#----------------
#EE 381 fall 2020
#Project 2
#Nhan Vo
#I.D. #017771388
#Start Date: 9-9-2020
#End Date:
#Simulation of a coin flip. Use simulation to determine probability of
#heads on an odd flip.
#----------------
import random# import random module
p= float()
for i in range(10):#count controlled loop and range function
    r=random.uniform(0,1)
    if r<p:
        print("Heads")
    else:
        print("Tails")




