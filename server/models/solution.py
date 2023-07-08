
# Solutions for user problems
import json


class Solution:
    solution_id = None
    rating_id   = None
    content     = ""


    def __init__(self,i_solutionID,i_ratingID,s_content) -> None:
        self.solution_id = i_solutionID
        self.content = s_content
        self.rating_id = i_ratingID

    
    def tojson(self) -> json:
        return json.dumps({'id': self.solution_id, 'content':self.content, 'raitingID':self.rating_id})
        


