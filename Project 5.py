#EE 381 fall 2020 Project 5
#Name: Nhan Vo
#I.D.#:017771388
#Start Date: 11-16-2020
#End Date:
#Description: Simulation of a random walk
#----------------------------------------
import random
p= float(input("What is the probability of a forward step?: "))

N=int(input("what is the last state?: "))

S= int(input("Beginning state: "))

J=int(input("How many 'steps' will be taken? "))

#----------------------------------------

for i in range(J):
    if S==0:
        S=1
    elif S==N:
        S=N-1
    elif (S<N)and (S>0):
        r=random.uniform(0,1)
        if r<p:
            S=S+1
        else:
            S=S-1
    print(S)
