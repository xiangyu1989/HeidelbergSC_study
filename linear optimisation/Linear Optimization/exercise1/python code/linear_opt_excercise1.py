# -*- coding: utf-8 -*-
# This script is for the linear optimisation exerciese 1 

# Author: Yu Xiang, student number: 897864
import math 
import numpy as np

################################################################################
##### M1
A_ls = [[1, 2], [3, 0]]
A = np.array(A_ls)
b_ls = [1, 3]
b = np.array(b_ls)
B_ls = [[4, 6, 8], [11, 2, 12], [3, 5, 16]]
B = np.array(B_ls)
u_ls = [4, 6, 8]
u = np.array(u_ls)
c = np.dot(u, B)
c_ewp = u * B

print ( 'c is' + str(c))
# B 3 * 3 matrix, u_T 3 * 1 matrix, d should also be 3 * 1 matrix
d = np.dot(B, np.transpose(u))
d = np.transpose(np.matrix(d))
print ( 'd is' + str(d))


# c should be 1 * 3 matrix, d should be 3 * 1 matrix
# in order to ensure that c and d has the right matrix dimension, we converts 
c = np.matrix(c)

e = np.dot(c, d)
print ( 'e is' + str(e))

F = np.dot(d, c)
print ( 'F is' + str(F))

G = np.dot(c.T, d.T).T
print ( 'G is' + str(G))



###############################################################################
##### M2 

A = np.array( [[2, 4, -2], [4, 9, -3], [-2, -3, 7]])
A = np.matrix(A)
y = np.array([2, 8, 10])
y = np.matrix(y)
x = A.I * y.T   # A.I is to retrive the inverse matrix A
print ( 'X is' + str(x))

###############################################################################
##### M3 

a = [2, 4, -6]
a1 = a[0]
a2 = a[1]
a3 = a[2]

 



r = np.roots([2, 4, -6])
print (r)



'''
b = np.matrix(b_ls)
B_ls = [[4, 6, 8], [11, 2, 12], [3, 5, 16]]
B = np.matrix(B_ls)
u_ls = [4, 6, 8]
u = np.matrix(u_ls)
# u = np.transpose(u)

## Output: 
# c = u * B; 
c = u * B
print ('c is \n' + str(c) +'\n')
d = B * np.transpose(u)
print ('d is \n' + str(d) +'\n')
e = c * d;
F = d * c;
G = np.transpose(np.transpose(c) * np.transpose(d))


print (u.ndim, u.shape, B.shape)
u.shape

print ('c is \n' + str(c) +'\n', 'd is \n' + str(d) +'\n',
'e is \n' + str(e) +'\n', 'F is \n' + str(F) +'\n', 'G is \n' + str(G) +'\n')


# c = np.dot(u, B)
d = np.transpose(np.dot(B, np.transpose(u))); 
e = np.dot(c, d);
F = np.dot(d, c);
G = np.transpose(np.dot(np.transpose(c), np.transpose(d)))
print (u.ndim, u.shape, B.shape)
u.shape

print ('c is \n' + str(c) +'\n', 'd is \n' + str(d) +'\n',
'e is \n' + str(e) +'\n', 'F is \n' + str(F) +'\n', 'G is \n' + str(G) +'\n')


b = [1, 3]'; 
B = [4, 6, 8; 11, 2, 12; 3, 5, 16]; 
u = [4, 6, 8]; 

% Output: 
% M1 a)
c = u * B; 
% M1 b)
d = B * u'; 
% M1 c)
e = c * d;
% M1 d)
F = d * c;
% M1 e)
G = (c'*d')'; 
'''
