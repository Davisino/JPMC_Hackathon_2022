from dataclasses import dataclass
import imp
from pyexpat import model
import re

from database.rating import getRating

from database.user import getUser
from database.problem import getProblem
from database.ratesolutions import getSolution
import datetime
import models.question
import database.db as db


# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True

# gets a random question based on the current time
def GetOpenQuestion(db_name):
    curr_time = datetime.datetime.now()
    
    morning_time = curr_time.replace(hour=6, minute=0, second=0, microsecond=0)
    evening_time = curr_time.replace(hour=12, minute=0, second=0, microsecond=0)
    night_time = curr_time.replace(hour=23, minute=59, second=0, microsecond=0)
    afternoon_time = curr_time.replace(hour=6, minute=0, second=0, microsecond=0)

    if(curr_time > night_time and curr_time <= morning_time):
        return GetMorningOpenQuestion(db_name)
    elif(curr_time > morning_time and curr_time <= afternoon_time):
        return GetAfternoonOpenQuestion(db_name)
    elif(curr_time > afternoon_time and curr_time <= evening_time):
        return GetEveningOpenQuestion(db_name)
    elif(curr_time > evening_time and curr_time <= night_time):
        return GetNightOpenQuestion(db_name)
    else:
        return GetNightOpenQuestion(db_name)


# GetMorningOpenQuestion will be returned if time is between 6am - 12am 
def GetMorningOpenQuestion(database_name):
    if(__DEBUG__MODE__):
        print("debug: "," Get Morning Open Question was called")

    return db.getOpenQuestion(database_name,"Morning") 


# GetEveningOpenQuestion will be returned if time is between 6pm - 12am 
def GetEveningOpenQuestion(database_name):
    if(__DEBUG__MODE__):
        print("debug: "," Get Evening Open Question was called")

    return db.getOpenQuestion(database_name,"Evening")
    

# GetNightOpenQuestion will be returned if time is between 12am - 6am 
def GetNightOpenQuestion(database_name):
    if(__DEBUG__MODE__):
        print("debug: "," Get Night Open Question was called")

    return db.getOpenQuestion(database_name,"Night")

# GetAfternoonOpenQuestion will be returned if time is between  12am - 6 pm
def GetAfternoonOpenQuestion(database_name):
    if(__DEBUG__MODE__):
        print("debug: "," Get Afternoon Open Question was called")

    return db.getOpenQuestion(database_name,"Afternoon")


def GetProblem(database_name,i_problem_id):
    if(__DEBUG__MODE__):
        print("debug: "," Get Problem with id", i_problem_id, " Was called")
    
    return getProblem(database_name,i_problem_id)
    

def GetUser(database_name, userID):
    if(__DEBUG__MODE__):
        print("debug: "," Get User with id", userID, " Was called")
    
    return getUser(database_name,userID)


def GetSolution(database_name, solutionID):
    if(__DEBUG__MODE__):
        print("debug: "," Get Solution with id", solutionID, " Was called")
    
    return getSolution(database_name,solutionID)


def GetRating(database_name, ratingID):
    if(__DEBUG__MODE__):
        print("debug: "," Get Rating with id", ratingID, " Was called")
    
    return getRating(database_name,ratingID)