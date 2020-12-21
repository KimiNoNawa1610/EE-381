#EE 381 fall 2020 Project 4
#Name: Nhan Vo
#I. D# 017771388
#End Date:
#Simulate a continuos RV.

import math#Math functions
import random# Pseudorandom numbers
import matplotlib.pyplot as pdf#Alias probability density function, pdf

n=10000# number of iterations
Lambda=1#Parameter in exponetial distribution.
x=[]#List for uniformally distributed random numbers.
y=[]#List for exponentially distributed random numbers.


for i in range(n):
    r=random.uniform(0,1)#Generate random numbers
    x.append(r)# List of Uniformally distributed random numbers.
    e=-(1/Lambda)*math.log(1-r,math.e)
    y.append(e)#List of exponetially distributed random numbers.
    
b=max(x)
a=min(x)
R=b-a#Range
intervals=int(math.ceil(math.sqrt(n)))#These are the classes (bins)
width=(R/intervals)#The class width.



pdf.subplot(2,1,1)
pdf.hist(x,intervals,density=width)# Uniform Simulation
pdf.subplot(2,1,2)
pdf.hist(y,intervals,density=width)# Exponential Simulation

