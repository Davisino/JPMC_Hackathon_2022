import json
from logging import error
import random
import sqlite3
from sqlite3 import Connection, Cursor, Error
import uuid

from models.question import Question

# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True

# create_connection will create a connection from a database 
# name and will return the open connection
def create_connection(s_db_file) -> Connection:
    """ create a database connection to a SQLite database 
        creates a new database if the given one doesn't exist """
    conn = None

    conn = sqlite3.connect(s_db_file)

    if(conn == None):
        print("FAILED to establish connection")
        return

    if (__DEBUG__MODE__ ):
        print(sqlite3.version)
    
    return conn


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


def insertIssueType(s_db_file, s_content, issueType):
    if (s_db_file == None):
        print("There was an error on insertion.", "connection is None")
        return

    # if(s_timeOfDay != "Morning" or s_timeOfDay != "Evening" or s_timeOfDay != "Night" or s_timeOfDay != "Afternoon"):
    #     print("There was an error on formatting.","time of day is in the wrong format, please check it")
    #     return

    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if (cursor == None):
        print("There was an error on creating cursor.", "cursor is None")
        return

    sql = ''' INSERT INTO issueTypes(qid,qcontent,qtod)
                VALUES(?,?,?) '''

    random_id = uuid.uuid1()
    question = (str(random_id), s_content, issueType)

    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()

    if (__DEBUG__MODE__):
        print("Success: Finished uploading open question to db")
    conn.close()

    return json.dumps({'status': 200})

def getAnswerSymptoms(s_db_file, symptom):
    try:
        conn = create_connection(s_db_file)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM issueTypes WHERE qtod=?", (symptom,))

        rows = cursor.fetchall()
        # index = random.randrange(0, len(rows), 1)
        #
        # question = rows.pop(index)
        #
        # q = Question(question[0], question[1], question[2])

        return rows

    except Error as e:
        if (__DEBUG__MODE__):
            print("Failed to get an answer", e)

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


# setUpInitialdb will set up some initial tables that are needed 
# this function will create those tables if they dont already exist
def setUpInitialdb(p_connection):

    try:
        
        cursor = p_connection.cursor()
       

        if (__DEBUG__MODE__ ):
            print("Building New Database")
    

        default_tables = {
            '''
            CREATE TABLE IF NOT EXISTS openQuestions([qid] TEXT, [qcontent] TEXT, [qtod] TEXT)
            ''',
            '''
            CREATE TABLE IF NOT EXISTS ratings([rid] INTEGER PRIMARY KEY AUTOINCREMENT, [rvalue] INTEGER, [rfrequency] INTEGER) 
            ''',
            '''
            CREATE TABLE IF NOT EXISTS solutions([sid] INTEGER PRIMARY KEY AUTOINCREMENT, [scontent] TEXT, [sratingid] INTEGER) 
            ''',
            '''
            CREATE TABLE IF NOT EXISTS problems([pid] INTEGER PRIMARY KEY, [pcontent] TEXT, [psolutionid] INTEGER) 
            ''',
            '''
            CREATE TABLE IF NOT EXISTS users([uid] INTEGER PRIMARY KEY, [uname] TEXT, [usecondname] TEXT,
            [gender] TEXT,[age] INTEGER,[username] TEXT,[password] TEXT, [email] TEXT, problemSet TEXT)
            ''',
            '''
              CREATE TABLE IF NOT EXISTS issueTypes([qid] , [qcontent] TEXT, [qtod] TEXT)
            ''',
            }
        
        for table in default_tables:
            cursor.execute(table)
            p_connection.commit()
            
        if (__DEBUG__MODE__ ):
            print("Tables Updated, Built New Database")
        
        p_connection.close()
    except Error as e:
        if (__DEBUG__MODE__ ):
            print("Failed to set up the database connection" , e)

    

    
    
