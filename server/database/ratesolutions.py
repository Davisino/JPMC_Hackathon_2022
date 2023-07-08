import json

from models.solution import Solution
from database.db import create_connection

# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True

def insertSolution(s_db_file,s_content,i_ratingID):
    
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    sql = ''' INSERT INTO solutions(scontent,sratingid)
                VALUES(?,?) '''

    solution = (s_content,i_ratingID)
     
    cur = conn.cursor()
    cur.execute(sql, solution)
    conn.commit()

    if (__DEBUG__MODE__ ):
            print("Success: Finished uploading solution to db")
    conn.close()

    return json.dumps({'status':200})

def updateRating(s_db_file,i_ratingID,i_ratingValue):
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


def getSolution(s_db_file,i_solution_id):
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    cursor.execute("SELECT * from solutions WHERE sid=?",(i_solution_id,))
    
    rows = cursor.fetchall()

    solution = rows.pop(0)
    soltn = Solution(solution[0],solution[1],solution[2])

    return soltn.tojson()