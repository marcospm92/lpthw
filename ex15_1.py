# import argv to use it later
from sys import argv

# first "thing" you wrote when calling this file is script, and second is filename
script, filename = argv

# it opens "filename" and saves it into txt
txt = open(filename)

# prints something with the name of the file.
print(f"Here's your file {filename}:")
# reads "txt" and prints it.
print(txt.read())
# closes txt.
txt.close()

print("Type the filename again:")
# ask the user to print again the filename and saves it in file_again
file_again = input("> ")
# opens file_again and saves it into txt_again
txt_again = open(file_again)

# reads txt_again and prints it.
print(txt_again.read())
# closes txt_again
txt_again.close()
