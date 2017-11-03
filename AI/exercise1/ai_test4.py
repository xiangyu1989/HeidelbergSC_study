# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:19:14 2017

@author: DELL
"""

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
data=np.arange(900).reshape((30,30))
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(data)

plt.suptitle('Main title')
plt.show()   
