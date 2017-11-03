# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 22:43:33 2017

@author: DELL
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab


user_input = 0
mean = float(user_input)
mu = mean
stds = [0.5, 2]
sigma = stds[0]
sigma2 = stds[1]

sigma_large = max(stds)
print (sigma_large)

x = np.linspace(mu - 3*sigma_large, mu + 3*sigma_large, 100)

y1 = mlab.normpdf(x, mu, sigma)
y2 = mlab.normpdf(x, mu, sigma2)

locs = ["upper left", "lower left", "center right"]
f, axarr = plt.subplots(2, sharex=True)
f.suptitle("Gauss distribution with the same mean and different standard deviations", fontsize=16)
axarr[0].plot(x, y1, 'k--')
axarr[0].legend(['Mean : ' +  str(mean) + ' standard deviation: ' + str(stds[0])])
axarr[0].legend(loc = locs[0])
# axarr[0].legend()
axarr[1].plot(x, y2, 'k:')
axarr[1].legend(['Mean : ' +  str(mean) + ' standard deviation: ' + str(stds[1])])
axarr[1].legend(loc = locs[0])