#Many real-world situations involve more than two possible conditions. For example, consider an amusement park that charges different rates for different age groups:
# - Admission for anyone under the age of 4 is free.
# - Admission for anyone between the ages of 4 and 18 is $25.
# - Admission for anyone age 18 or older is $40.
age = 12 
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the if-elif-else chain and then have a simple print() call that runs after the chain has been evaluated:
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print("\n"f"Your admission cost is ${price}.")

# Using Multiple elif Blocks
# You can use as many elif blocks in your code as you like. For example, the amusement park can add a discount for seniors:
age = 77
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: 
    price = 20

print("\n"f"Your admission cost is ${price}.")

# Omitting the else Block
# Python does not require an else block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest:
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print("\n"f"Your admission cost is ${price}.")

# Testing Multiple Conditions 
# The if-elif-else chain is powerful, but it's only appropriate to use when you need just one test to pass. As soon as Python finds one test that passes, it skips the rest of the test. This behavior is beneficial, because it's efficient and allows you to test for one specific condition. 