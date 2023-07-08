
# Rating linked to a solution
import json


class Rating:
    rating_id       = None
    rating_value    = None
    rating_chosen_frequency = None


    def __init__(self,i_ratingID,i_rating_value,i_rating_chosen_frequency) -> None:
        self.rating_id = i_ratingID
        self.rating_value = i_rating_value
        self.rating_chosen_frequency = i_rating_chosen_frequency

    
    def tojson(self) -> json:
        return json.dumps({'id': self.rating_id, 'ratingvalue':self.rating_value, 'ratingfrequency':self.rating_chosen_frequency})
        


