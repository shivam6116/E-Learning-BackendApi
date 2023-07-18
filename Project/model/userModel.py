import json
import mysql.connector
from flask import make_response

class userModel():
    def __init__(self) -> None:
        
        #connection code
        print("creating")
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="P@ssword191394",database="flask_project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)

        except:
            print("some error")
        

    def user_signup_model(self):
        return "this is sign up class"

    def getUsers(self):
        
        self.cur.execute("SELECT * FROM USERS")
        result = self.cur.fetchall()
        if(len(result)>0):
            return make_response({"payload":result},200)

            ''' 
            json.dumps(result): this return the result in list formate
            '''
        else:
            return make_response({ "Message":"No data"},204)

    def add_user(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}'   )")
        return make_response({ "Message":"User Added"},201)
        
        
    def update_user(self,data):
        # print(data)
        self.cur.execute(f"UPDATE users SET name='{data['name']}' ,email='{data['email']}' ,phone='{data['phone']}' ,role ='{data['role']}' ,password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Updated"},201)
        else:
            return make_response({ "Message":"nothing to update"},202)
    
    def delete_user(self,id):
        # print(data)
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Deleted"},200)
        else:
            return make_response({ "Message":"nothing to nothingf to delete"},202)
    