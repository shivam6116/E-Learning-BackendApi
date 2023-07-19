import mysql.connector
from flask import make_response

class RolesModel():
    def __init__(self) -> None:
        
        #connection code
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="P@ssword191394",database="flask_project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection Successful")

        except:
            print("some error")

    def getAllRoles(self):

        self.cur.execute("SELECT * FROM roles")
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

    def add_roles(self,data):
        self.cur.execute(f"INSERT INTO roles(title) VALUES('{data['title']}')")
        return make_response({ "Message":"User Added"},201)
    
       
    def update_roles(self,data):
        self.cur.execute(f"UPDATE roles SET title='{data['title']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"Role Updated"},201)
        else:
            return make_response({ "Message":"nothing to update"},202)  

    
    def delete_roles(self,id):
        self.cur.execute(f"DELETE FROM roles WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Deleted"},200)
        else:
            return make_response({ "Message":"nothing to delete"},202)