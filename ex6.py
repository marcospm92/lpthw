# defines a variable
types_of_people = 10
# inserts the variable in a string variable with f-string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# prints both string variables.
print(x)
print(y)

# Inserts a string inside a print
print(f"I said: {x}")
print(f"I also said: '{y}'.")

# boolean variable, T/F
hilarious = False
# Interesting way of re-using a string. I leave {} empty
joke_evaluation = "Isn't that joke so funny?! {}"
# and now with print(.format) I can assign a variable to the previous string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# combining variables inside a print to get a longer string
print(w + e)
