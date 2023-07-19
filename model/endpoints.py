
import mysql.connector
from flask import make_response

class EndPointsModel():
    def __init__(self) -> None:
        
        #connection code
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="P@ssword191394",database="flask_project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection Successful")

        except:
            print("some error")


    def getAllEndPoints(self):

        self.cur.execute("SELECT * FROM endpoints")
        result = self.cur.fetchall()
        if(len(result)>0):
            res=make_response({"payload":result},200) # sending response object
            res.headers['Access-Control-Allow-Origin']="*"    # to allow cross plateform response
            return res
        else:
            return make_response({ "Message":"No data"},204)


    def add_endPoints(self,data):
        self.cur.execute(f"INSERT INTO endpoints(endpointscol,methods) VALUES('{data['endpointscol']}', '{data['methods']}' )")
        return make_response({ "Message":"User Added"},201)
    
   
    def update_endpoints(self,data):
        '''
        User should provide id of endpoint with the data
        '''
        self.cur.execute(f"UPDATE endpoints SET endpointscol='{data['endpointscol']}',methods='{data['methods']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"Role Updated"},201)
        else:
            return make_response({ "Message":"nothing to update"},202)  

    
    def delete_endpoints(self,id):
        self.cur.execute(f"DELETE FROM endpoints WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({ "Message":"User Deleted"},200)
        else:
            return make_response({ "Message":"nothing to delete"},202)
