import os
import openai
import wandb




openai.api_key = "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"


# user class for guests and returning users (logged in users)
class User:
    'A User class'
    user_type = 0

    # initialization or constructor method of
    def __init__(self):  
 
        self.firstname = "Josh"
        self.surname = "Man"
        #user demographics
        self.gender = "man"
        self.age = "27"
        self.username = ""

        #decide which type of user it is
        if(self.firstname == "" and self.surname == ""):
            User.user_type = 0
        else:
            User.user_type = 1

  
    def retrieveReturningUser(self):
        print(self.firstname)
        print(self.surname)
        print(self.gender)
        print(self.age)

    def retrieveGuestUser(self):
        print(self.gender)
        print(self.age)

    # generate random username
    def generateUsername(self):
        
        #data to feed the model
        data = "Generate a single funny username that contains a random personality trait, a random item and a random 3 digit number. The username must be work-appropriate.\n"
        
        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=data,
          temperature=0.7,
          max_tokens=256,
          top_p=1,
          frequency_penalty=2,
          presence_penalty=2
        )
        if 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text']
            else:
                answer = 'Oh no something went wrong!'
        else:
            answer = 'Oh no something went wrong!'

        print(answer)

    # generate personlized punchline - take into consideration username, mental health issue, progress
    # move this function from here to another file
    def generateFeedback(self):
        # retrieve data from pickle file on how the user is feeling
        user_answer = "Yes"
        data = "User is feeling sad today. User has the following conditions: anxiety. If user has done the recommendations, then AI will congratulate the user called ditzy_donut_937, will make a joke about a donut and say the number of monsters the user fought against today. If the user has done the recommendations, then the AI will create a funny rhyme. If user hasn't done the recommendations then AI will tell him off and try to convince the user to finish the recommendations first by giving the user reasons why it would be helpful for him and display a list of resources related to the user's feelings, as well as making a rhyme with his user name. The list must include links to the resource. The list of resources is only given if user said No. The user has fought against 1 monster(s) today. The AI is very funny, cheeky and silly.\nCreate personalized feedback for the user. Make the feedback as funny as possible. The AI must include a rhyme.\n\"AI: Have you completed the recommendations I suggested?\nUser: " + user_answer +"/. Start the answer without including AI.\n\"\n",
        
        response = openai.Completion.create(
          model="text-davinci-002",
          prompt=data,
          temperature=0.7,
          max_tokens=302,
          top_p=1,
          frequency_penalty=1.48,
          presence_penalty=0.39
        )
        if 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text']
            else:
                answer = 'Oh no something went wrong!'
        else:
            answer = 'Oh no something went wrong!'
        
        return answer
        


