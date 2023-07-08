import json

from models.user import User
from database.db import create_connection

# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True


def insertNewUser(s_db_file,userID,first_name,surname,gender,age,username,password,email,problemSet):
    
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    sql = ''' INSERT INTO users(uid,uname,usecondname,gender,age,username,password,email,problemSet)
                VALUES(?,?,?,?,?,?,?,?,?) '''


    user = (userID,first_name,surname,gender,age,username,password,email,problemSet) 
    cursor.execute(sql, user)
    conn.commit()
    
    if (__DEBUG__MODE__ ):
            print("Success: Finished uploading user to db")
    conn.close()

    return json.dumps({'status':200})


def getUser(s_db_file,userID):

    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    cursor.execute("SELECT * from users WHERE uid=?",(userID,))
    
    rows = cursor.fetchall()

    newuser = rows.pop(0)
    user = User(newuser[0],newuser[1],newuser[2],newuser[3],newuser[4],newuser[5],newuser[6],newuser[7])

    return user.tojson()