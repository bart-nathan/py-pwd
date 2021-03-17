#!/usr/bin/python3

import os
import sys
import sqlite3

def exec_db(sql_statement):

        result = []

        conn = sqlite3.connect('pwmdb_test.db')
        cur = conn.cursor()
        cur.execute(sql_statement)

        if sql_statement[0] == 'i' or sql_statement[0] == 'd' or sql_statement[0] == 'u' or sql_statement[0] == 'c':
            conn.commit()
            
        elif sql_statement[0] == 's':
            
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

                print("%s   |   %s  | %s" % (item[0], item[1], item[2]))
               
        elif command == "insert":

            sitename = sys.argv[2]
            username = sys.argv[3]
            password = sys.argv[4]
            link = sys.argv[5]

            exec_db("insert into record (sitename, username, password, link) values ('%s', '%s', '%s', '%s')" % (sitename, username, password, link))

        elif command == "get":

            id = sys.argv[2]
            
            found_record = exec_db("select * from record where id = %s" % id)

            for item in found_record:
                print(item) 

        elif command == "update":

            id = sys.argv[2]

            if id != 0:

                sitename = sys.argv[3]
                username = sys.argv[4]
                password = sys.argv[5]
                link = sys.argv[6]

                sql = "update record set sitename = '%s', username = '%s', password = '%s', link = '%s' where id = %s " % (sitename, username, password, link, id)
                print(sql)
                exec_db(sql)
            
        
        
        elif command == "delete":

           id = sys.argv[2]

           if id != 0:
               
               exec_db("delete from record where id = %s" % id)


        elif command == "create":

            table = "create table record (id integer not null primary key autoincrement,sitename varchar(100) not null,username varchar(100) not null,password varchar(100) not null,link varchar(300) not null);"
            exec_db(table)
            
        else:
            
            print("No command is found :-(")

    except Exception as ex:
        print(ex)
    
    print("Ok\n");