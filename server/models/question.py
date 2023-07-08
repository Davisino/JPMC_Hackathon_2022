
# Question, what we will ask the user at each point
import json


class Question:
    question_id = ""
    content= ""
    time = ""
   

    def __init__(self,s_questionID,s_content,t_time) -> None:
        self.question_id = s_questionID
        self.content = s_content
        self.time = t_time

    
    def tojson(self) -> json:
        return json.dumps({'id': self.question_id, 'content':self.content, 'time':self.time})
        


