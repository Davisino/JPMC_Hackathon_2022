import datetime

# import api

class Question():

    def get_time(self):
        now = datetime.time()
        return now

    def time_in_range(self, start, end, x):
        """Return true if x is in the range [start, end]"""
        if start <= end:
            return start <= x <= end
        else:
            return start <= x or x <= end  

    def time_dependant_question(self, current_time):
        
        if self.time_in_range(datetime.time(5,0,0), datetime.time(12,0,0), current_time):
            # message = get_morning_question()
            message = "good morning, how are you feeling?"
        elif self.time_in_range(datetime.time(12,0,0), datetime.time(18,0,0), current_time):
            # message = get_afternoon_question()
            message = "good afternoon, how are you feeling?"
        elif self.time_in_range(datetime.time(18,0,0), datetime.time(0,0,0), current_time):
            # message = get_evening_question()
            message = "Good evening, how are you feeling?"
        else:
            pass
        return message

    def get_opening_question(self):
        # question = api.get_question()
        time = self.get_time()
        question = self.time_dependant_question(time)
        return question

    def get_answers(self):
        answers = ["Good","Bad", "I'm Okay", "Can't complain"]
        return answers

    def save_answer(self, answer):
        # api.push(answer)
        return answer

    def question_2_res(self):
        #problem_list = api.get_problem_list()
        problem_list = ["sleep", "depression", "self-harm"]
        return problem_list

    def process_problem(self, answer):
        #send emotion to api
        monster_emotion = answer
        return monster_emotion

    def question_2(self):
        # question = api.get_question2()
        question = "what are you currently suffering from?"
        return question

# first_q = get_opening_question()
# print(first_q)
# answers = get_answers()
# print(answers)
# question_2 = question_2()
# print(question_2)
# responses = question_2_res()
# print(responses)
# chosen_response = input("respond\n")
# monster_emotion = process_problem(chosen_response)
# print(monster_emotion)




    

