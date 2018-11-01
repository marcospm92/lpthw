from sys import argv

script, filename = argv

print(f"This is the content of the file {filename}: ")

file = open(filename)
print(file.read())

print("End of the file.")
