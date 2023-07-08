import json

from models.problem import Problem
from database.db import create_connection

# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True

def insertProblem(s_db_file,problem_id,content,solution_id):
    
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    sql = ''' INSERT INTO problems(pid,pcontent,psolutionid)
                VALUES(?,?,?) '''

    problem = (problem_id,content,solution_id)
     
    cur = conn.cursor()
    cur.execute(sql, problem)
    conn.commit()

    if (__DEBUG__MODE__ ):
            print("Success: Finished uploading problem to db")
    conn.close()

    return json.dumps({'status':200})


def getProblem(s_db_file,problem_id):
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    cursor.execute("SELECT * from problems WHERE pid=?",(problem_id,))
    
    rows = cursor.fetchall()

    problem = rows.pop(0)
    prb = Problem(problem[0],problem[1],problem[2])

    return prb.tojson()


 #def updateRating(s_db_file,i_ratingID,i_ratingValue):
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    sql = ''' UPDATE ratings SET rvalue = ? WHERE rid = ? '''

    newRating = (i_ratingValue,i_ratingID)
     
    cur = conn.cursor()
    cur.execute(sql, newRating)
    conn.commit()

    if (__DEBUG__MODE__ ):
            print("Success: Finished updating rating and uploading to db")
    conn.close()

    return json.dumps({'status':200})