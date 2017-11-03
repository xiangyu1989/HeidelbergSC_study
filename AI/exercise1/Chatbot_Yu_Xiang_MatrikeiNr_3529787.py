#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Artificial Intelligence
Prof. Björn Ommer
WS17/18

Exercise sheet 1 - Question 1

@author: Uta Büchler

# Solution by: Yu Xiang, Matrikei. Nr: 3529787, Email: shawnxiangyu@yahoo.com
# Python version 3.6
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

random.seed()

class Chatbot():
    
    def __init__(self,greetings,questions,reaction,farewells,questions_user=None,answers=None):
        '''
        Initialize the chatbot given the input arguments
        (is called when creating an object of the class Chatbot)
        
        input:  greetings:      list of strings - predefines which greetings the bot can use
                questions:      list of strings - predefines the questions the bot can ask
                reaction:       function - decides how to react to the answers made by the user
                questions_user: list of strings - predefines which questions the user might ask the bot (Ex. 1b)
                answers:        list of strings - predefines the answers of the bot given a specific question of the user
                farewells:      list of strings - predefines how the bot can say goodbye
        
        '''
        self.reaction = reaction#function 
        self.greetings = greetings
        self.questions = questions
        self.questions_user = questions_user
        self.answers = answers
        self.farewells = farewells
        #during the conversation the bot has to ask all questions
        #question index is removed in askQuestion() if question was asked
        self.notAsked = range(0,len(questions))
        self.shownGauss = 0#boolean - has to be changed to 0 for Question 1c
    
    def greeting(self):
        '''
        Question 1a)
        The bot outputs randomly a greeting given all possible greetings in self.greetings
        Afterwards, the bot asks for the name of the user and reacts by saying 'Nice to meet you USER',
        where USER has to be replaced by the input made from the user.

        Question 1b)
        After greeting the user the Bot has to check if the user asked questions during his last input.
        If yes, he has to answer them. For extracting the different parts of the users input (in case
        he asked a question) you can use self.extractParts(user_input,delimiter)
        '''
        
        greeting_list = self.greetings 
        greeting_random = random.choice(greeting_list)
        print (greeting_random)
        
        ask_names = ['What is your name?', 'How should i call you?', 'What\'s your name?']
        ask_names_random = random.choice(ask_names)
        print (ask_names_random)
        greeting_answers = input('User input:  ')
                
        if self.isQuestion(greeting_answers):             
           extracted_answer = self.extractParts(greeting_answers, '.')           
           print ('Nice to meet you ' , extracted_answer[0])           
           answer = self.answerQuestion(extracted_answer[1])
           print (answer)
        else: # this is not a question, assuming the user only answer the name
            print ('Nice to meet you ', greeting_answers)
            return     
        
    def askQuestion(self):
        '''
        Question 1a)
        The bot outputs randomly a question given all possible questions in self.questions
        If the question was asked, it should be removed from the variable self.notAsked.
        Afterwards, the bot should react to the answer of the user by using the input of the user.
        Example: 
            Question_bot: What are your hobbies? 
            Answer_user: football, meeting friends
            Reaction_Bot: I don't like football, but I like meeting friends
            
        How the bot reacts to which question has to be given by the function self.reaction
        For extracting the different parts of the answer (1st part is 'football', second is 'meeting friends')
        you can use the function self.extractParts()
        '''
        notAsked = self.notAsked # this is a range or a list
        self_questions = self.questions
        
        notAsked_list = list(notAsked)
        ask_random = random.choice(notAsked_list)
        
        question_toAsked = self_questions[ask_random]
        print (question_toAsked)
        
        notAsked_list.remove(ask_random)
        self.notAsked = notAsked_list       
        
        answer_from_user = input('User input:  ')
        
        # If the user reaction contains both an answer and a question. 
        # Assuming '.' is used to seperate the answer and question from the user. The question is ended with a '?' mark
        # Otherwise, if the reaction contains only an answer, then the answer is ended either with a '.' or no marks at all. 
        
        answer_parts = self.extractParts(answer_from_user, '.')  
        reaction(self, question_toAsked, answer_parts[0])
        
        if self.isQuestion(answer_from_user):  
            answer = self.answerQuestion(answer_parts[1])
            print (answer)
        
        '''
        Question 1b)
        After reacting to the answer of the user the Bot has to check if the user asked questions during his last input.
        If yes, he has to answer them. For extracting the different parts of the users input (in case
        he asked a question) you can use self.extractParts(user_input,delimiter)
        '''
        
    def farewell(self):
        '''
        Question 1a)
        The bot outputs randomly a farewell given all possible greetings in self.farewells
        '''
        farewells_list = self.farewells
        farewell_random = random.choice(farewells_list)
        print (farewell_random)
        
                                 
    def extractParts(self,user_input,delimiter,outputType = str):
        '''
        Find the different parts of the users input, by splitting the string 'user_input' in its parts
        using the delimiter specified as input. If necessary, the output can be of a different type than
        string (for example float)
               
        
        Input:
            user_input: input made by the user
            delimiter:  substring which identifies the end and start of a part
            outputType: type of the elements in the output list 'parts'
        
        Output:
            parts: list of strings - contains the parts of the user's input in the sepecified type
        '''
        parts = [outputType(x.strip()) for x in user_input.split(delimiter)]       
        return parts
    
    def answerQuestion(self,user_input):
        '''
        Question 1b)
        This function finds the appropriate answer to the question(s) made by the user.
        First, the question has to be find in self.questions_user. This then leads to the index
        needed to find the right answer of the bot using self.answers.
        
        Input: user_input: list of strings - contains the parts of the user's input
        Output: answers: all answers to the questions made from the user in his/her current input
        
        # user_input is pre-defined questions. 
    
        '''
        answers = []       
        questions_user = self.questions_user                     
        if user_input in questions_user:
            user_qs_index = questions_user.index(user_input)              
            answers = self.answers[user_qs_index]
            
        else: 
            # the question the user asked must be among the pre-defined questions, 
            # Otherwise, the chat bot can not find the matching answer 
            answers = 'Sorry, I do not understand your question!'      
        return answers    
    
    def isQuestion(self,user_input):
        '''
        Question 1b)
        This function checks if the user asked a question during his last input.
        Input:  user_input: list of strings - contains the parts of the user's input
        Output: a boolean variable, stating if one of the user_input parts contains a questionmark or not
        '''
        end_mark = user_input[-1]
        if end_mark == '.': 
            return False
        elif end_mark == '?':
            return True
        else:
            # print ('Could not tell whether it is a question or a statement. Assuming by default it is a statement!')
            return False            

    def plotGauss(self):
        '''
        Question 1c)
        This function let the chatbot plot two Gauss Curves given a mean and two different standard deviations
        chosen by the user.
        
        Use the function "norm" from the library scipy.stats to compute the function values y1 and y2
        given x, the mean and the two standard deviations std1 and std2
        Plot both functions (as subplots) using the library matplotlib.pyplot.
        Play a little bit around with the properties one can set for the plots
        (like setting a title,changing the line color etc etc)
        '''
        self.shownGauss = 1
        user_input= input("Do you want to see how a Gauss curve looks like? \n")
        if user_input.lower()=='yes':
            user_input = input("Cool! Then you need to give me a random number between 0 and 1 for the mean \n")
            mean = float(user_input)
            user_input = input("I want to show you 2 Gaussians with different standard deviations. So I need two numbers now between 0 and 1 \n")
            stds = self.extractParts(user_input,',',outputType=float)
                        
            max_stds = max(stds)     
            
            x = np.linspace(mean - 3 * max_stds, mean + 3 * max_stds, 100)           
            y1 = mlab.normpdf(x, mean, stds[0])
            y2 = mlab.normpdf(x, mean, stds[1])   
            
            #  plot the two Gauss distribution in the plot
            f, sub_plots = plt.subplots(2, sharex=True)
            f.suptitle("Gauss distribution with the same mean, different standard deviations", fontsize=12)
            sub_plots[0].plot(x, y1, 'k--')
            sub_plots[0].set_ylabel('distribution density')
            sub_plots[0].legend(['Mean : ' +  str(mean) + ' standard deviation: ' + str(stds[0])])
            sub_plots[1].plot(x, y2, 'k:')
            sub_plots[1].set_ylabel('distribution density')
            sub_plots[1].legend(['Mean : ' +  str(mean) + ' standard deviation: ' + str(stds[1])])
            plt.show()
            
        elif user_input.lower()=='no':
            print ("Oh... ok.")
            
    def main(self):
        '''
        main function to perform the conversation between chatbot and user
        starts with greeting, then asks all available questions and ends with a farewell
        ll../[;/]
        The part with the Gauss curve only applies for Question 1c.
        Change the boolean variable self.shownGauss to 0, so that the function plotGauss will be executed
        during the conversation.
        '''
        self.greeting()
        while not len(self.notAsked)==0:#ask questions until all questions are asked
            self.askQuestion()
            if not self.shownGauss:#plot Gauss if it hasn't been done already
                prob = 1 if len(self.notAsked)==0 else random.randint(0,1)#plot with probability of 50% or 100% if last question was asked
                if prob: self.plotGauss()
        self.farewell()


if __name__ == "__main__":
    
    def reaction(bot, question, answer):       
        '''
        Question 1a)
        Determines the reaction of the chatbot to an answer given by the user after the bot asked a question
        Input:
            bot:        Object of the class Chatbot
            question:   string - containing the question the bot asked
            answer:     string - containing the answer of the user to the question of the bot
        Output: nothing - the output/reaction should be printed in the console
        '''
        
        bot_question = bot.questions
        if question in bot_question:
            user_qs_index = bot_question.index(question) 
            # pre_defined bot_questions = ['What do you do?','What\'s your plan for the weekend?','What is your hobby?'],
            
            if user_qs_index == 0 :
                print ('Wow, my sibling has the same job too.')
            elif user_qs_index == 1 :
                print ('What a coincidence, I have the same plan for the weekend as you.')
            elif user_qs_index == 2 :
                if len(answer) > 1: 
                    # if the answer has string length larger than 1, we take the last wrod of the string                  
                    extracted_ans = bot.extractParts(answer, ' ')
                else: 
                    extracted_ans = answer
                print ('Awesome! I like '+ extracted_ans[-1] + ' as well. We could have fun together then!')                                 
        else: 
            print('Wow, that is interesting!')        
        return 

    
    bot = Chatbot(greetings = ['Hi!','Hi there!', 'Hello there!'],
              questions = ['What do you do?','What\'s your plan for the weekend?','What is your hobby?'],
              reaction = reaction,
              questions_user = [ 'What are you busy with nowadays?','How is the weather there?','Shall we hang out some time?', 'BTW, what is your name?'],            
              answers =  ['I am occupied with talking to you!','It is great. Sunny and Warm!','Definitely!', 'You can call Xiang.' ],
              farewells = ['Someone is ringing the bell. I will see you then.','I have a call coming, I will talk to you later','Nice talking to you, but my class will begin soon. I have to leave now. Bye'])
    bot.main()
