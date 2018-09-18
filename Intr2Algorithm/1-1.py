#Problems 1-1
#For each function f(n) and time t in the following table, determine the largest
#size n of a problem that can be solved in time t , assuming that the algorithm to
#solve the problem takes f(n) microseconds.

import math
from sympy import *


#Transfer time to microseconds
t=[]
t.append({'one_sec':1e6})
t.append({'one_min':60*1e6})
t.append({'one_hour':60*60*1e6})
t.append({'one_day':60*60*24*1e6})
t.append({'one_month':60*60*24*30*1e6})
t.append({'one_year':60*60*24*30*12*1e6})
t.append({'one_cent':60*60*24*30*12*100*1e6})

print('the largest size of n when the algorithm is lg n :')
for x in t:
    print(list(x)[0],': 10^',list(x.values())[0],sep='')

print('the largest size of n when the algorithm is the root of n :')
for x in t:
    root_n=(list(x.values())[0])**2
    print(list(x)[0],':',root_n,sep='')

print('the largest size of n when the algorithm is n :')
for x in t:
    n=list(x.values())[0]
    print(list(x)[0],':',n,sep='')


#define nlgn function, inspired from https://github.com/pezy/AlgorithmNotes/blob/master/Foundations/overview/calc.py   
def n_lgn(c):
    lower = 0.0
    upper = 10e13
    while True:
        middle = (lower + upper) / 2
        if lower == middle or middle == upper:
            return middle
        if middle * math.log(middle, 2) > c:
            upper = middle
        else:
            lower = middle


print('the largest size of n when the algorithm is n lg n:')
for x in t:
    n=n_lgn(list(x.values())[0])
    print(list(x)[0],':',n,sep='')


print('the largest size of n when the algorithm is sqrt of n :')
for x in t:
    n=list(x.values())[0]**0.5
    print(list(x)[0],':',n,sep='')

print('the largest size of n when the algorithm is thrid power of n :')
for x in t:
    n=list(x.values())[0]**(1/3)
    print(list(x)[0],':',n,sep='')

print('the largest size of n when the algorithm is the nth power of 2 :')
for x in t:
    n=log(list(x.values())[0],2)
    print(list(x)[0],':',float(n),sep='')

# n!
def n_factorial(c):
    n = 0
    while True:
        if math.factorial(n) >= c:
            return n - 1
        else:
            n += 1

print('the largest size of n when the algorithm is factorial of n :')
for x in t:
    n=n_factorial(list(x.values())[0])
    print(list(x)[0],':',int(n),sep='')