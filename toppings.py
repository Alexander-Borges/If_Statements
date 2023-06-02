# When you want to determine whether two values are not equal, you can combine an exclamation point and an equal sign (!=). The exclamation point represents not, as it does in many programming languages.
requested_topping ='mushrooms'
if requested_topping !="anchovies":
    print('Hold the anchovies!')
# Because the value of requested_topping is not "anchovies", the print() function is executed/

# Sometimes it's important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks.

requested_toppings = ['mushrooms','extra cheese']

if"mushrooms" in requested_toppings:
    print(f"Adding {requested_toppings[0]}")
if"pepperoni" in requested_toppings:
    print("Adding pepperoni")
if"extra cheese" in requested_toppings:
    print(f"Adding {requested_toppings[1]}")

print("\nFinished making your pizza!")

# Checking for special items
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping =="green peppers":
        print("Sorry we are out of green peppers right now.") 
    else:
        print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza!")

# Checking that a list is not empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print('\nFinished making your pizza!')
else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we do not have {requested_topping}")

print("\nFinished making your pizza!")
    