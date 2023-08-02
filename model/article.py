import mysql.connector

class article():
    def __init__(self) -> None:
        
        #connection code
        print("creating")
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="abc191394",database="project")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)

            # self.cur.execute("CREATE TABLE article (  id INT NOT NULL AUTO_INCREMENT,  username VARCHAR(255) NOT NULL,  email VARCHAR(255) NOT NULL,  PRIMARY KEY (id))")

        except:
            print("some error")


# obj=article()