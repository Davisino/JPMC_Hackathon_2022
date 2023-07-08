
#  User details
import json


class User:
    userID  = 0
    first_name = ""
    surname = ""
    gender  = ""
    age = 0
    username = ""
    password = ""
    email  = ""
    problemSet = ""

    def __init__(self,i_userID, i_age, s_gender,s_firstname = None, s_surname = None,
     s_email=None,s_username = None, s_password = None) -> None:

        self.userID  = i_userID
        self.first_name = s_firstname
        self.surname = s_surname
        self.gender  = s_gender
        self.age = i_age
        self.username = s_username
        self.password = s_password
        self.email  = s_email
        self.problemSet = ""



    def tojson(self) -> json:
        return json.dumps({'id': self.userID, 'age': self.age, 'gender': self.gender, 'firstname': self.first_name,'secondname': self.surname,
        'email':self.email, 'username': self.username, 'pass': self.password})
        


