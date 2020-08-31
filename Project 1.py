##EE 381 fall 2020 Project 1
#Name: Nhan Vo
#I.D:017771388
#The code for pseudorandom number generator is in this file
#and it is used to do sumple simulation.

def main():
    import math

    def RNG():

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
        for k in range(25):
            d=math.floor(6*r[k]+1)
            print(d)

    def coin(r):
        print("Coin Flip Below ")
        for k in range(25):
            c=math.floor(2*r[k])
            print("head") if c==1 else print("tale")

    s=RNG()
    die(s)
    coin(s)

main()
