from flask import Flask, jsonify
import server_requests.get.requests as get_request
import server_requests.put.requests as put_request
import database.db as db

app = Flask(__name__)
db_name = "db_monsterhack.sqlite"

questions = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]





# Issues DB
@app.route('/monsterhack/api/v1.0/issueType/<tod>')
def getanswersymptoms(tod):
   return db.getAnswerSymptoms(db_name, tod)
@app.route('/monsterhack/api/v1.0/putonissuetype/<content>/<tod>')
def putonissuetype(content,tod):
   return db.insertIssueType(db_name,content,tod)



@app.route('/monsterhack/api/v1.0/questions', methods=['GET'])
def get_tasks():
    return jsonify({'questions': questions})

# First question screen, Get question with time
@app.route('/monsterhack/api/v1.0/getopenquestion')
def getopenquestion():
   return get_request.GetOpenQuestion(db_name)


@app.route('/monsterhack/api/v1.0/putopenquestion/<content>/<tod>')
def putopenquestion(content,tod):
   return db.insertOpenQuestion(db_name,content,tod)


# update a solution rating to a problem
@app.route('/monsterhack/api/v1.0/updatesolutionrating/<ratingID>/<rating>')
def updateSolutionRating(ratingID,rating):
   return put_request.updateSolutionRating(db_name,ratingID,rating)


# inserts a new solution
@app.route('/monsterhack/api/v1.0/putsolutionrating/<content>/<rating>')
def putsolutionrating(content,rating):
   return put_request.putNewSolutiom(db_name,content,rating)


# inserts a new problem
@app.route('/monsterhack/api/v1.0/putnewproblem/<problemid>/<content>/<solutionid>')
def putNewProblem(problemid,content,solutionid):
   return put_request.putNewProblem(db_name,problemid,content,solutionid)


# inserts a new user with all info
@app.route('/monsterhack/api/v1.0/putnewuser/<userID>/<first_name>/<surname>/<gender>/<age>/<username>/<password>/<email>/<problemSet>')
def putnewuser(userID,first_name,surname,gender,age,username,password,email,problemSet):
   return put_request.putnewuser(db_name,userID,first_name,surname,gender,age,username,password,email,problemSet)
   

# gets a new user with all info
@app.route('/monsterhack/api/v1.0/getuser/<userID>')
def getUser(userID):
   return get_request.getUser(db_name,userID)

# gets a problem with info
@app.route('/monsterhack/api/v1.0/getproblem/<problemid>')
def GetProblem(problemid):
   return get_request.GetProblem(db_name,problemid)


# gets a solution with all info
@app.route('/monsterhack/api/v1.0/getsolution/<solutionid>')
def GetSolution(solutionid):
   return get_request.GetSolution(db_name,solutionid)

# gets a solution with all info
@app.route('/monsterhack/api/v1.0/getrating/<ratingid>')
def getRating(ratingid):
   return get_request.GetRating(db_name,ratingid)

if __name__ == '__main__':
    conn = db.create_connection(db_name)
    db.setUpInitialdb(conn)
    app.run(debug=True)