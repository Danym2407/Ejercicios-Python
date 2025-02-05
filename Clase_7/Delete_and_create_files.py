# Delete and create files

import os


# Delete if exists
if os.path.exists("helloWorld.txt"):
    os.remove("helloWorld.txt")
else:
    print("The file doesn't exists. Turururururu")
    
    
f = open("helloWorld.txt", "x") # Create the document
f.write("Hello World")
f.close
 

f = open("helloWorld.txt", "r") # Create the document   
print(f.read())
f.close()

    





