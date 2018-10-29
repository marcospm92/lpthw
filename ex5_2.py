name = 'Zed A. Shaw'
age = 35 # not a lie
height_in = 74 # inches
weight_lb = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = 2.54 * height_in
weight_kg = 0.453592 * weight_lb
print(f"Let's talk about {name}.")
print(f"He's {height_in} inches or {height_cm} centimeters tall.")
print(f"He's {weight_lb} pounds or {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to gei it exactly right
total_in_lb = age + height_in + weight_lb
print(f"If I add {age}, {height_in}, and {weight_lb} I get {total_in_lb}.")
total_cm_kg = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total_cm_kg}.")
