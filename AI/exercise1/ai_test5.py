# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:19:59 2017

@author: DELL
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.mlab as mlab



# Simple data to display in various forms
#x = np.linspace(0, 2 * np.pi, 400)
#y = np.sin(x ** 2)

user_input = 0
mu = float(user_input)
#user_input = input("I want to show you 2 Gaussians with different standard deviations. So I need two numbers now between 0 and 1 \n")
# stds = self.extractParts(user_input,',',outputType=float)

stds = [0.5, 2]
sigma = stds[0]
sigma2 = stds[1]

sigma_large = max(stds)
print (sigma_large)
x = np.linspace(mu - 3*sigma_large, mu + 3*sigma_large, 100)
y1 = mlab.normpdf(x, mu, sigma)
y2 = mlab.normpdf(x, mu, sigma2)





fig, axarr = plt.subplots(2, 1)
fig.suptitle("This Main Title is Nicely Formatted", fontsize=16)

axarr[0, 0].plot(x, y1)
axarr[0, 0].set_title('Axis [0,0] Subtitle')
axarr[0, 1].plot(x, y2)

#axarr[0, 1].set_title('Axis [0,1] Subtitle')
#axarr[1, 0].plot(x, y ** 2)
#axarr[1, 0].set_title('Axis [1,0] Subtitle')
#axarr[1, 1].scatter(x, y ** 2)
#axarr[1, 1].set_title('Axis [1,1] Subtitle')

# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=True)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=True)

# Tight layout often produces nice results
# but requires the title to be spaced accordingly
fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()