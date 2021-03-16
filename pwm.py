#!/usr/bin/python3

import os
import sys


if __name__ == "__main__":

    try:
        
        command = sys.argv[1]

        if command == "list":

            print("list records")
        
        elif command == "get":

            print("Get command")

        elif command == "update":

            print("updatecommand")
        
        elif command == "delete":

            print("delete command")
        else:
            
            prinf("No command is found :-(")

    except:
        print("error :-)")

    

 

    
    
    
    
    print("Ok\n");