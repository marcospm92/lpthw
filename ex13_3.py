from sys import argv
# read the WYSS section for how to run this
script, first = argv

inp = input("Insert variable: ")
print("The script is called:", script)
print("Your variable of argv is:", first)
print("Your variable of input is:", inp)
