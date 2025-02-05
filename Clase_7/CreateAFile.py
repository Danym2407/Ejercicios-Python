# Files exercises

"""
    File Handling
        * r = read
        * a = append
        * w = write
        * x = create
        
    How it should be handled
        * t = text
        * b = binary
        
"""

# To open a file
f = open("helloWorld.txt", "x") # We create de file
f.write("HELLO WORLD.") # Write
f.close() # Close the file


f = open("helloWorld.txt", "r")
contenido = f.read()
f.close()

if contenido:
    print(contenido)
else:
    print('Empty File')


