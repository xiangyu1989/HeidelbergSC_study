# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:44:39 2017

@author: 
Alex Romelt, Matrikei. Nr:  , Email: 
Alex Vonig,  Matrikei. Nr:  , Email: 
Yu Xiang, ,  Matrikei. Nr: 3529787,  Email: shawnxiangyu@yahoo.com  

"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets
iris = sklearn.datasets.load_iris()
iris = iris.data 

numcols = len(iris[0]) # get the number of attribute

print ('Iris data summary statistics is shown here')
# print the empiricial mean and standard deviation of each attribute
print ('The empirical mean of each attribute is: ',  np.mean(iris, 0))
print ('The empirical standard deviation of each attribute is: ', np.std(iris, 0))

# boxplot for the Iris data
plt.figure()
plt.boxplot(iris, 1)

# calcualte the (Pearson) correlation between the attributes
corr_matrix = np.corrcoef(np.transpose(iris))


print ('The corrleation matrix is as: ', corr_matrix)

largest_pcorr = 0  # initilize a variable to find the largest non-negative correlation coefficients
location = [0, 0]

# find the location where the highest positive correlation coefficients locate
for i in range(1, numcols):
    for j in range (0, i):
        if corr_matrix[i,j] > largest_pcorr:           
            largest_pcorr = corr_matrix[i,j]
            print (largest_pcorr)
            location = [i, j]
            
print ('the largest non-negative correlation coefficient is: ', largest_pcorr)

# plot a scatter of the two attributes with the highest positive correlation coefficients
plt.figure()
plt.scatter(iris[:,location[0]], iris[:,location[1]])
plt.xlabel('Attribute: ' + str(location[0] + 1))

        
