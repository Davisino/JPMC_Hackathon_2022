import json

from models.rating import Rating
from database.db import create_connection

# When this is turned on, we want to export all log info to console
__DEBUG__MODE__ = True


# returns rating entity
def insertRating(s_db_file,i_ratingValue,i_rating_efficency):
    
    if(s_db_file == None):
        print("There was an error on insertion.","connection is None")
        return
    
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    if(cursor == None):
        print("There was an error on creating cursor.","cursor is None")
        return

    sql = ''' INSERT INTO ratings(rvalue,rfrequency)
                VALUES(?,?) '''

    rating = (i_ratingValue,i_rating_efficency)
     
    cur = conn.cursor()
    cur.execute(sql, rating)
    conn.commit()

    if (__DEBUG__MODE__ ):
            print("Success: Finished uploading rating to db")
    conn.close()

    return getRatingEntity(s_db_file)


# gets last entity by default
def getRatingEntity(s_db_file, search_id):
    conn = create_connection(s_db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ratings WHERE rid=?",(search_id,))
    rows = cursor.fetchall()

    return rows.pop()


def getRating(s_db_file, search_id):
    res = getRatingEntity(s_db_file,search_id)

    return Rating(res[0],res[1],res[2]).tojson()

