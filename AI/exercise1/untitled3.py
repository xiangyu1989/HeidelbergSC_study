# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 22:39:39 2017

@author: DELL
"""

         mean = float(user_input)
            user_input = input("I want to show you 2 Gaussians with different standard deviations. So I need two numbers now between 0 and 1 \n")
            stds = self.extractParts(user_input,',',outputType=float)
                        
            max_stds = max(stds)     
            
            x = np.linspace(mean - 3 * max_stds, mean + 3 * max_stds, 100)           
            y1 = mlab.normpdf(x, mean, stds[0])
            y2 = mlab.normpdf(x, mean, stds[1])   
            
            #  plot the two Gauss distribution in the plot
            f, axarr = plt.subplots(2, sharex=True)
            f.suptitle("Gauss distribution with the same mean and different standard deviations", fontsize=16)
            axarr[0].plot(x, y1, 'k--')
            axarr[0].legend(['Mean : ' +  str(mean) + ' standard deviation: ' + str(stds[0])])
            axarr[1].plot(x, y2, 'k:')
            axarr[1].legend(['Mean : ' +  str(mean) + ' standard deviation: ' + str(stds[1])])