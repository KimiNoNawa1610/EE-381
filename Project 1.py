##EE 381 fall 2020 Project 1
#Name: Nhan Vo
#I.D:017771388
#The code for pseudorandom number generator is in this file
#and it is used to do sumple simulation.

def PseudoGenerator():
    N=10000#Cycle length or norm
    A=4857#Adder
    M=8601#Multiplier

    S= int(input("Enter a whole number"))
    term= int (input("Please enter your nth that you want to run"))
    for i in range(term):
        S=(M*S+A)%N
        r=S/N#The number r will be in [0,1)
        print(format(r,'.4f'))

PseudoGenerator()
