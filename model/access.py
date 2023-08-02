
import mysql.connector
from flask import make_response

class AccessModel():
    def __init__(self) -> None:
        
        #connection code
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="abc191394",database="project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection Successful")

        except:
            print("some error")



    def getAllaccess(self):

        self.cur.execute("SELECT * FROM access")
        result = self.cur.fetchall()
        if(len(result)>0):
            res=make_response({"payload":result},200) # sending response object
            res.headers['Access-Control-Allow-Origin']="*"    # to allow cross plateform response
            return res
        else:
            return make_response({ "Message":"No data"},204)


    def add_Access(self,data):
        print(data)
        self.cur.execute(f"INSERT INTO access (endpoint_id,roles) VALUES('{data['endpoint_id']}', '{data['roles']}' )")
        return make_response({ "Message":"Access Added"},201)
    

    def update_Access(self,data):
        '''
        User should provide id of endpoint_id with the data
        '''
        self.cur.execute(f"UPDATE access SET endpoint_id='{data['endpoint_id']}',roles='{data['roles']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"Role Updated"},201)
        else:
            return make_response({ "Message":"nothing to update"},202)  

    
    def delete_Access(self,id):
        self.cur.execute(f"DELETE FROM access WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Deleted"},200)
        else:
            return make_response({ "Message":"nothing to delete"},202)
