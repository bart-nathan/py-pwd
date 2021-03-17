#!/usr/bin/python3

import os
import sys
import sqlite3

def exec_db(sql_statement):

        result = []

        conn = sqlite3.connect('pwmdb.db')
        cur = conn.cursor()
        cur.execute(sql_statement)
        conn.commit()
    
        for item in cur:
            result.append(item)

        conn.close()

        return result;

if __name__ == "__main__":

    try:

        command = sys.argv[1]

        if command == "list":

            result = exec_db("select * from record");

            for item in result:

                print(item)
               
        elif command == "insert":

            sitename = sys.argv[2]
            username = sys.argv[3]
            password = sys.argv[4]
            link = sys.argv[5]

            exec_db("insert into record (sitename, username, password, link) values ('%s', '%s', '%s', '%s')" % (sitename, username, password, link))

            #print("insert command is here :-)")
        
        elif command == "get":

            print("Get command")

        elif command == "update":

            print("updatecommand")
        
        elif command == "delete":

            print("delete command")
        else:
            
            prinf("No command is found :-(")

    except Exception as ex:
        print(ex)
    
    print("Ok\n");