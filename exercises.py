# 1 Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
i = 'programmer'
print("Am i == 'programmer'? I predict True")
print(i == 'programmer')

best_player = 'Shohei'
print("Is Shohei == 'best_player'I predict True")
print(best_player=='Shohei')

best_player = 'Shohei'
print("Is Judge == 'best_player'? I predict False")
print(best_player =='Judge')

# 2 More conditional Tests: 
# - Test for equality and inequality with strings
string1 = "Hello"
string2 = "World"

if string1 == string2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

string1 = "Hello"
string2 = "Hello"

if string1 != string2:
    print("The strings are not equal.")
else:
    print("The strings are equal.")

# - Test using the lower() method.
best_player = 'Messi'
print('\n',best_player.lower() =='messi')

# - Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
x = 5
y = 10

# Equality test
print(x == y)

# Inequality test
print(x != y)

# Greater than test
print(x > y)

# Less than test
print(x < y)

# Greater than or equal to test
print(x >= y)

# Less than or equal to test
print(x <= y)

# - Test using the and keyword and the or keyword 
x = 5
y = 10
z = 7

# 'and' test
if x > 0 and y > 0:
    print("Both x and y are greater than 0.")

# 'or' test
if x > 0 or z > 0:
    print("Either x or z is greater than 0.")

# - Tell whether an item is in a list
favorite_teams = ['dodgers','chargers','lakers']
print("dodgers".title() in favorite_teams)
print("yankees" in favorite_teams)

epl_teams = ["Arsenal","Chelsea","Manchester City"]
la_liga_team = "Barcelona"
if la_liga_team not in epl_teams:
    print(f"{la_liga_team} is not in the English Premier League.")

# 3 Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of "green","yellow", or "red".
# - Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output)
alien_color = 'green'
if alien_color == "green":
    print("\nYou just earned 5 points!")

alien_color = 'red'
if alien_color =='green':
    print("You just earned 5 points!")

# 4 Alien Colors #2: Choose a color for an alien as you did in exercise 3, and write an if-else chain.
# - If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
# - If the alien's color isn't green, print a statement that the player just earned 10 points.
# - Write one version of this program that runs the if block and another that runs the else block. 
alien_color = 'yellow'
if alien_color =='green':
    print("\nYou just earned 5 points for shooting the alien")
else:
    print("\nYou just earned 10 points!")

# Alien Colors #3: Turn your if-else chain from Exercise 4 into an if-elif-else chain.
# - If the alien is green, print a message that the player earned 5 points
# - If the alien is yellow, print a message that the player earned 10 points. 
# - If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate alien.
alien_color = "green"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == "yellow":
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")

alien_color = "yellow"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == "yellow":
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")

alien_color = "red"

if alien_color == "green":
    print("Congratulations! You just earned 5 points for shooting the green alien.")
elif alien_color == "yellow":
    print("Congratulations! You just earned 10 points for shooting the yellow alien.")
else:
    print("Congratulations! You just earned 15 points for shooting the red alien.")

# 6 Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
# if the person is less than 2 years old, print a message that the person is a baby.
# if the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# if the person is at least 4 years old byt less than 13, print a message that the person is a child.
# if the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# if the person is at least 20 years old but less than 65, print message4 that the person is an adult.
# if the person is 65 or older print a message that the person is an elder.
age = 32
if age < 2: 
    person = 'baby'
elif age >= 2 and age < 4:
    person = 'toddler'
elif age >=4 and age < 13:
    person = 'child'
elif age >= 13 and age <20:
    person = 'teenager'
elif age >=20 and age <65:
    person = 'adult'
elif age >=65:
    person = 'elder'

print(f"\nThis is person is in the {person} stage of life.")

# 7 Hello Admin: Make a list of five usernames, including the name "admin". Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop thru the list, and print a greeting to each user:
# - If the username is admin print a special greeting, such as Hello Admin, would you like to see a status report?
# - Otherwise, print a generic greeting, such as hello Alex, thank you for logging in again.
users = ['admin','alex','jessica','rachel','adam']
for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else: 
        print(f"Hello {user.title()}, thank you for logging in again.")

# 8 No Users: Add an if test to make sure the list of users is not empty. 
# - if the list is empty, print the message We need to find some users!
users = []
if len(users) == 0:
    print("We need to find some users!")

current_users = ['alex','tom','brian','taylor','ashley']
new_users = ['tom','sam','roger','peter','taylor']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"Sorry, the username '{user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")

# Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except for 1,2,and 3/
# store the numbers 1 thru 9 in a list.
# loop thru the list
# Use an if-elif-else chain inside the loop to print the proper original ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
