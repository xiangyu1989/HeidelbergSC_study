# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:46:25 2017

@author: DELL
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab


#user_input = input("I want to show you 2 Gaussians with different standard deviations. So I need two numbers now between 0 and 1 \n")
# stds = self.extractParts(user_input,',',outputType=float)


        # try to extract the names and questions 
        # assuming in the greeting part, the user will not ask any questions!
        # answer_parts = self.extractParts(answer_with_names)    

user_input = 0
mu = float(user_input)
stds = [0.5, 2]
sigma = stds[0]
sigma2 = stds[1]

sigma_large = max(stds)
print (sigma_large)

x = np.linspace(mu - 3*sigma_large, mu + 3*sigma_large, 100)

y1 = mlab.normpdf(x, mu, sigma)
y2 = mlab.normpdf(x, mu, sigma2)


#plt.plot(x,y1, x, y2)
#plt.show()


   # check whether the question asked by the user is among the pre-defined user questions
   question_by_user = extracted_answer[1]
   questions_user = self.questions_user
   
   # print (question_by_user)
   # print (questions_user)
   
   if question_by_user in questions_user:
   user_qs_index = questions_user.index(question_by_user)
   
   print (user_qs_index)
   print (self.answers[user_qs_index])
   return
   # print ('This is for test')
   else: 
   # the question the user asked must be among the pre-defined questions, 
   # Otherwise, the chat bot can not find the matching answer 
   print('Sorry, I do not understand your question.')
   return
   # self.askQuestion           




if self.isQuestion(answer_from_user):        
answer_parts = self.extractParts(answer_from_user)  

reaction(self, answer_parts, self.answers)
answers = self.answerQuestion(answer_parts[1])            
print(answers)


#np.random.seed(0)
#
#x, y = np.random.randn(2, 100)
#fig = plt.figure()
#ax1 = fig.add_subplot(211)
#
#ax1.xcorr(x, y1, usevlines=True, maxlags=50, normed=True, lw=2)
#ax1.grid(True)
#ax1.axhline(0, color='black', lw=2)
#
#ax2 = fig.add_subplot(212, sharex=ax1)
#ax2.acorr(x, y2, usevlines=True, normed=True, maxlags=50, lw=2)
#ax2.grid(True)
#ax2.axhline(0, color='black', lw=2)
#
#plt.show()



# Two subplots, the axes array is 1-d
f, axarr = plt.subplots(2, sharex=True)
f.suptitle("This Main Title is Nicely Formatted", fontsize=16)
axarr[0].plot(x, y1, 'k--', label='Model length')
axarr[0].legend(['A simple line'])
# axarr[0].set_title('Gaussian with mean 0 and std ' + str(0.5) + '(top) and ' + str(2) + '(bottom)')
axarr[1].plot(x, y2)
axarr[1].legend(['A second line'])

'''
x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
plt.plot(x_axis, norm.pdf(x_axis,0,2))
'''
