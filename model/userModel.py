import json
from turtle import done
import mysql.connector
from datetime import datetime, timedelta
from flask import make_response
import jwt

class userModel():
    def __init__(self) -> None:
        try:
            
            self.con=mysql.connector.connect(host="localhost",username="root",password="abc191394",database="project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)

        except:
            print("some error")
        

    def getUsers(self):
        
        self.cur.execute("SELECT * FROM USERS")
        result = self.cur.fetchall()
        if(len(result)>0):
            res=make_response({"payload":result},200) # sending response object
            res.headers['Access-Control-Allow-Origin']="*"    # to allow cross plateform response
            return res
            ''' 
            json.dumps(result): this return the result in list formate
            '''
        else:
            return make_response({ "Message":"No data"},204)

    def add_user(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['password']}'   )")
        return make_response({ "Message":"User Added"},201)
        
        
    def update_user(self,data):
        # print(data)
        self.cur.execute(f"UPDATE users SET name='{data['name']}' ,email='{data['email']}' ,phone='{data['phone']}' ,password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Updated"},201)
        else:
            return make_response({ "Message":"nothing to update"},202)
    
    def delete_user(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Deleted"},200)
        else:
            return make_response({ "Message":"nothing to nothingf to delete"},202)
    

    def patch_user(self,data,id):
        query="UPDATE users SET "
        for key in data:
            query= query + f" {key} = '{data[key]}' ,"
            # print()
        
        query=query[:-1]
        query+= f"WHERE id={id}"
        print(query)

        self.cur.execute(query)
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Updated Using Patch"},200)
        else:
            return make_response({ "Message":"nothing to nothingf to delete"},202)

    def pagination_user(self,limit ,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit

        query=f"SELECT * FROM users LIMIT {start},{limit}"

        self.cur.execute(query)
        result = self.cur.fetchall()
        if(len(result)>0):
            res=make_response({"payload":result},200) # sending response object
            res.headers['Access-Control-Allow-Origin']="*"    # to allow cross plateform response
            return res
            ''' 
            json.dumps(result): this return the result in list formate
            '''
        else:
            return make_response({ "Message":"No data"},204)


    def addUserAvatar(self,uid,path):
        self.cur.execute(f"UPDATE users SET avatar= '{path}' where id={uid}")
        return "done"


    def user_login(self,data):
        self.cur.execute(f"SELECT id ,email , phone, avatar, roll_id FROM users WHERE email='{data['email']}' and password ='{data['password']}'")
        result =self.cur.fetchall()
        userData=result[0]


        expTime= datetime.now() +timedelta(minutes=15)
        expEpochTime=int(expTime.timestamp())

        payload={
            "payload":userData,
            "exp":expEpochTime
        }

        token=jwt.encode(payload, "shivam", algorithm="HS256")

        return make_response({"token":token})