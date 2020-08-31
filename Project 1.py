##EE 381 fall 2020 Project 1
#Name: Nhan Vo
#I.D:017771388
#Start Date: 8-26-2020
#End Date: 8-31-2020
#The code for pseudorandom number generator is in this file
#and it is used to do sumple simulation.

def main():# main module
    import math

    def RNG():# pseudoRandomNumberGenerator

        r=[]#Empty list for our random numbers
        
        N=10000#Cycle length or norm
        A=4857#Adder
        M=8601#Multiplier

        S= int(input("Enter a whole number. "))
        for i in range(100):
            S=(M*S+A)%N#Our linear congrutenital pseudoRandomNumberGenerator
            v=S/N#The number r will be in [0,1)
            r.append(v)
        return r

    def die(r):#roll dice
        print("Die roll below")
        for k in range(25):#roll 25 time
            d=math.floor(6*r[k]+1)#linear transformation
            print(d)

    def coin(r):#flip coin
        print("Coin Flip Below ")
        for k in range(25):#flip 25 time
            c=math.floor(2*r[k])#linear transformation
            print("head") if c==1 else print("tail")

    s=RNG()# 's' is list of random numbers
    die(s)# Call to die function
    coin(s)#Call to coin function

main()
