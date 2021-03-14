# Use these classes to insert into database schemas 
from flaskApp import db
from random import randint

class User:
    def __init__(self, firstName, lastName, username, email, password):
        self.name = firstName + " " + lastName
        self.fname = firstName
        self.lname = lastName
        self.uname = username
        self.email = email
        self.pwd = password

        # Create mysqldb cursor 
        cur = db.connection.cursor()
        
        #Generate 5 digit userid 
        uid = ""
        while True: 
            for i in range(5):
                uid += str(randint(0,9))
            # Check if uid is in use 
            sql = """
                    SELECT userid 
                    FROM user 
                    WHERE userid={}""".format(uid)
            print(sql)
            cur.execute(sql)
            '''
            If cursor finds user with same uid generated, break out of loop
            otherwise erase the uid generated and start loop over
            '''
            rows = cur.fetchall()
            if len(rows) == 0:
                break
            else:
                uid = ""
        
        #sql = "INSERT INTO user VALUES ({id}, {username}, {password}, {email}, {name})".format(id = uid, username = self.uname, password = self.pwd, email = self.email, name = self.name)
        sql = f"""
            INSERT INTO user 
            VALUES ({uid}, '{self.uname}', '{self.email}', '{self.pwd}','{self.name}')"""
        print(sql)
        cur.execute(sql) 
        db.connection.commit()

