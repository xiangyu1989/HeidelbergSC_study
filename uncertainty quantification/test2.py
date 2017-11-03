# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:19:20 2017

@author: DELL
"""



import math
import numpy as np
import matplotlib.pyplot as plt
a = 2.0 ; 
b = 1.0; 
x1 = np.zeros(50);

for i in range(0, 50): 
   a = a / 10.0    
   b = b / 10.0   
   x1[i] = math.ceil((1 + a)/(1 + b))
   if i > 0:        
       if x1[i] - x1[i-1] == -1:
           precision = i 
           break
print ('The machine precision is : ', precision)

# questions 3: 

def e_ty_series(x):
    n = 20
    tx = 0.0
    for i in range(0, n):
        tx = tx + x ** i / math.factorial(i) 
        # print (tx) 
    return tx 

# print (e_ty_series(10))       
# print (e_ty_series(1))
print (e_ty_series(-1))       
# print (e_ty_series(-10))


def exponential(x):
    return math.exp(x)

def Taylor_exp(x,n):
    c = 0
    for i in range(n+1):
        temp = x**i/math.factorial(i)
        c = c + temp
    return c

def Taylor_exp_new(x,n):
    if x > 0:
        return Taylor_exp(x,n)
    else:
        return 1./Taylor_exp(-x,n)
    
#TEST:
x_list = [10,1,-1,-10]
relerr0 = []
relerr1  = []
relerr2 = []
relerr3 = []
#for x in x_list:

#for n in range(21):
#    relerr0.append(abs(Taylor_exp(x_list[0],n) - exponential(x_list[0]))/abs(x_list[0]))
#    relerr1.append(abs(Taylor_exp(x_list[1],n) - exponential(x_list[1]))/abs(x_list[1]))
#    relerr2.append(abs(Taylor_exp(x_list[2],n) - exponential(x_list[2]))/abs(x_list[2]))
#    relerr3.append(abs(Taylor_exp(x_list[3],n) - exponential(x_list[3]))/abs(x_list[3]))


for n in range(21):
    relerr0.append(abs(Taylor_exp_new(x_list[0],n) - exponential(x_list[0]))/abs(x_list[0]))
    relerr1.append(abs(Taylor_exp_new(x_list[1],n) - exponential(x_list[1]))/abs(x_list[1]))
    relerr2.append(abs(Taylor_exp_new(x_list[2],n) - exponential(x_list[2]))/abs(x_list[2]))
    relerr3.append(abs(Taylor_exp_new(x_list[3],n) - exponential(x_list[3]))/abs(x_list[3]))

n = list(range(21))
#print relerr0.shape
#print n.shape




fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].set_title('x = 10')
axes[0, 0].plot(n,relerr0,"b",linewidth=1)

axes[0, 1].set_title('x = -10')
axes[0, 1].plot(n,relerr3,"b--",linewidth=1)

axes[1, 0].set_title('x = 1')
axes[1, 0].plot(n,relerr1,"b",linewidth=1)

axes[1, 1].set_title('x = -1')
axes[1, 1].plot(n,relerr2,"g--",linewidth=1)
plt.show()

