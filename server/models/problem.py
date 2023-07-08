
# Problems users can work on
import json


class Problem:
    problem_id  = None
    content     = ""
    solution_id = None
   

    def __init__(self,s_problemID,s_content,s_solutionID) -> None:
        self.problem_id = s_problemID
        self.content = s_content
        self.solution_id = s_solutionID

    
    def tojson(self) -> json:
        return json.dumps({'id': self.problem_id, 'content':self.content, 'solutionid':self.solution_id})
        


