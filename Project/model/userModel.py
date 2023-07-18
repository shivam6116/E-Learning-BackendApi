import json
import mysql.connector


class userModel():
    def __init__(self) -> None:
        
        #connection code
        print("creating")
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="P@ssword191394",database="flask_project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("successful")

        except:
            print("some error")
        

    def user_signup_model(self):
        return "this is sign up class"

    def getUsers(self):
        
        self.cur.execute("SELECT * FROM USERS")
        result = self.cur.fetchall()
        if(len(result)>0):
            return json.dumps(result)
        else:
            return "No data"

    def add_user(self,data):
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}'   )")
        
        return "User Added"
        
    def update_user(self,data):
        # print(data)
        self.cur.execute(f"UPDATE users SET name='{data['name']}' ,email='{data['email']}' ,phone='{data['phone']}' ,role ='{data['role']}' ,password='{data['password']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "User Updated"
        else:
            return "nothing to update"
    
    def delete_user(self,id):
        # print(data)
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return "User Deleted"
        else:
            return "nothing to nothingf to delete"
    