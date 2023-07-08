import json
import random
import uuid

from models.question import Question
from database.db import create_connection

# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True

# insertOpenQuestion inserts a question entity into the openQuestion table 
# this value will be used at the begining of the game to start up the game
# s_timeOfDay MUST be Morning/Evening/Night/Afternoon
def insertOpenQuestion(s_db_file, s_content, s_timeOfDay):
    
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    # if(s_timeOfDay != "Morning" or s_timeOfDay != "Evening" or s_timeOfDay != "Night" or s_timeOfDay != "Afternoon"):
    #     print("There was an error on formatting.","time of day is in the wrong format, please check it")
    #     return

    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    sql = ''' INSERT INTO openQuestions(qid,qcontent,qtod)
                VALUES(?,?,?) '''


    random_id = uuid.uuid1()
    question = (str(random_id),s_content,s_timeOfDay)
     
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()

    if (__DEBUG__MODE__ ):
            print("Success: Finished uploading open question to db")
    conn.close()

    return json.dumps({'status':200})


def getOpenQuestion(s_db_file, s_timeOfDay):
    try:
        conn = create_connection(s_db_file)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM openQuestions WHERE qtod=?",(s_timeOfDay,))

        rows = cursor.fetchall()
        index = random.randrange(0,len(rows),1)

        question = rows.pop(index)
    
        q = Question(question[0],question[1],question[2])
        
        return q.tojson()

    except Error as e:
        if (__DEBUG__MODE__ ):
            print("Failed to get an open question" , e)
