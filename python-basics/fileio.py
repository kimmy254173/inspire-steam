# Name : Kimberley Gitau
# Date : 24/02/2026
# Program to perform file operations

# Create new file
new_file = open("student_data.txt","r+")

# Write to new file
new_file.write("{ Student Name : Alexis Keya, ID : 29783789, Email : kimmy@gmail.com }")


# Read from the file
new_file = open("student_data.txt","r+")


data = new_file.read()

print(data)

new_file.close()

# Delete file
# us os module
import os
os.remove("remove.txt")

# Delete folder
os.rmdir ("folder")