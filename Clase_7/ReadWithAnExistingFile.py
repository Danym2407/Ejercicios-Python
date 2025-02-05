
f = open("testingText.txt", "a")
f.write("""I would said that my favourite part of
        the movie is the concert but also the scene
        where Patrick dances through the soccer field
        """)
f.close()


f = open("testingText.txt", "r")
print(f.read())



"""
f = open("testingText.txt", "r")

# Print the whole text
for x in f:
  print(x) 
  
print(f.read(5)) # Prints the first 5 characters from the file
print("\n")
print(f.readline()) # print the first line
print("\n")
print(f.readline())  # print the second line
"""
