
import requests as req
import json
from types import SimpleNamespace
import random


class Monster:
    def __init__(self, name, issue):
        self.name = name
        self.issue = issue
    
    def __repr__(self):
        return f"Monster: {self.name}"
    
    # placeholder for the recommender function that gives a sorted list of recommended self care activities
    def sorted_self_care_activities(self):

        resp = req.get(f"http://localhost:5000/monsterhack/api/v1.0/issueType/{self.issue}")
        listOfBenefits = json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d))

        result = [0,0,0,0]
        i = 0
        print()
        while i < len(result):
            # Implement lottery for selecting random answer
            [_, benefit, category] = listOfBenefits[i]
            result[i] = self.purify(benefit)
            i+=1
        return result
    def purify(self, str):
        a = str.split('_')
        return " ".join(a)


