import json

from database.user import insertNewUser

from database.problem import insertProblem

from   database.rating import insertRating
import database.ratesolutions as db


def putNewSolutiom(db_name,content,rating):
    
    try:
       ratingInserted  = insertRating(db_name,rating,1)
       db.insertSolution(db_name,content,ratingInserted[0])

    except:
        print("couldn't put solution rating")
    

    return json.dumps({'status':200})



def updateSolutionRating(db_name,ratingID,ratingvalue):
    
    try:
       db.updateRating(db_name,ratingID,ratingvalue)
    except:
        print("couldn't put solution rating")
    

    return json.dumps({'status':200})



def putNewProblem(db_name,problem_id,content,solution_id):
    
    try:
       insertProblem(db_name,problem_id,content,solution_id)

    except:
        print("couldn't put insertProblem rating")
    

    return json.dumps({'status':200})

def putnewuser(s_db_file,userID,first_name,surname,gender,age,username,password,email,problemSet):
    try:
       insertNewUser(s_db_file,userID,first_name,surname,gender,age,username,password,email,problemSet)

    except:
        print("couldn't put new user into db")
    

    return json.dumps({'status':200})