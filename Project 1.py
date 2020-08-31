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
            S=(M*S+A)%N
            v=S/N#The number r will be in [0,1)
            r.append(v)
        return r

    def die(r):
        print("Die roll below")
        for k in range(25):#roll 25 time
            d=math.floor(6*r[k]+1)
            print(d)

    def coin(r):
        print("Coin Flip Below ")
        for k in range(25):#flip 25 time
            c=math.floor(2*r[k])
            print("head") if c==1 else print("tail")

    s=RNG()
    die(s)
    coin(s)

main()
